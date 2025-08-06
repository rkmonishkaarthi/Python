import os
import sys
import cv2
from ultralytics import YOLO
import ffmpeg
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

def run_detection(video_path):
    output_log = []

    # Step 1: Extract audio using ffmpeg
    output_log.append("🔊 Extracting audio for profanity detection...")
    
    # Create temporary files with proper paths
    temp_dir = tempfile.gettempdir()
    audio_path = os.path.join(temp_dir, "temp_audio.wav")
    converted_audio_path = os.path.join(temp_dir, "converted.wav")

    try:
        # Extract audio from video
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, acodec='pcm_s16le', ac=1, ar='16000')
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as e:
        output_log.append(f"Error extracting audio: {str(e)}")
        return "<br>".join(output_log)

    # Step 2: Convert to readable format if needed
    try:
        sound = AudioSegment.from_file(audio_path)
        sound.export(converted_audio_path, format="wav")
    except Exception as e:
        output_log.append(f"Error converting audio: {str(e)}")
        return "<br>".join(output_log)

    # Step 3: Transcribe audio using Google Web Speech API
    recognizer = sr.Recognizer()
    text = ""
    
    try:
        with sr.AudioFile(converted_audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio).lower()
        output_log.append(f"🎤 Transcribed text: '{text[:100]}...' (truncated)")
    except sr.UnknownValueError:
        text = ""
        output_log.append("⚠️ Could not understand audio.")
    except sr.RequestError as e:
        output_log.append(f"Google API error: {e}")
    except Exception as e:
        output_log.append(f"Speech recognition error: {e}")

    # Step 4: Check for profanity
    bad_words = [
        "damn", "hell", "shit", "fuck", "fucking", "bitch", "bastard", "asshole", "dick", "piss",
        "crap", "pussy", "cock", "slut", "whore", "violence", "kill", "murder", "rape", "terrorist"
    ]
    flagged_words = [word for word in bad_words if word in text]

    if flagged_words:
        output_log.append(f"⚠️ Profanity detected in audio: {flagged_words}")
    else:
        output_log.append("✅ No profanity detected in audio.")

    # Step 5: Run YOLOv8 for frame-level object detection
    # Note: Using pre-trained YOLOv8 model instead of custom violence detection model
    output_log.append("🔍 Running object detection on frames...")
    
    try:
        # Use pre-trained YOLOv8 model (downloads automatically if not present)
        yolo = YOLO("yolov8n.pt")  # Using nano version for faster inference
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            output_log.append("⚠️ Error: Could not open video file.")
            return "<br>".join(output_log)
        
        frame_count = 0
        detected_objects = []
        
        # Process every 30th frame for efficiency
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            if frame_count % 30 != 0:
                continue

            # Run YOLO inference
            results = yolo(frame, verbose=False)
            
            # Check for detected objects
            if results[0].boxes is not None and len(results[0].boxes) > 0:
                for box in results[0].boxes:
                    class_id = int(box.cls[0])
                    class_name = yolo.names[class_id]
                    confidence = float(box.conf[0])
                    
                    # Look for potentially violent objects/weapons
                    violent_objects = ['knife', 'gun', 'rifle', 'pistol', 'weapon']
                    if class_name.lower() in violent_objects and confidence > 0.3:
                        detected_objects.append(f"{class_name} (conf: {confidence:.2f})")
                        
        cap.release()
        
        if detected_objects:
            output_log.append(f"⚠️ Potentially violent objects detected: {', '.join(detected_objects)}")
        else:
            output_log.append("✅ No violent objects detected in video frames.")
        
    except Exception as e:
        output_log.append(f"Error during video analysis: {str(e)}")

    # Clean up temporary files
    try:
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(converted_audio_path):
            os.remove(converted_audio_path)
    except:
        pass  # Ignore cleanup errors

    return "<br>".join(output_log)
