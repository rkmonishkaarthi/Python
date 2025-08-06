"""
🚫 Restricted Content Detection for Google Colab
Run this script in Google Colab to detect restricted content in videos.

Instructions:
1. Copy this entire script
2. Paste it into a new Google Colab cell
3. Run the cell
4. Upload videos through the web interface that appears
"""

# ============================================================================
# STEP 1: Install Dependencies
# ============================================================================

print("🔧 Installing dependencies...")
import subprocess
import sys

def install_packages():
    """Install required packages in Colab"""
    packages = [
        'ultralytics', 'opencv-python', 'speechrecognition', 
        'pydub', 'ffmpeg-python', 'gradio'
    ]
    
    # Install system dependencies
    subprocess.run(['apt', 'update', '-qq'], check=True)
    subprocess.run(['apt', 'install', '-y', 'ffmpeg'], check=True)
    
    # Install Python packages
    for package in packages:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', package], check=True)
    
    print("✅ All dependencies installed!")

# Install packages
install_packages()

# ============================================================================
# STEP 2: Import Libraries
# ============================================================================

print("📥 Importing libraries...")

import os
import cv2
import tempfile
import gradio as gr
from ultralytics import YOLO
import ffmpeg
import speech_recognition as sr
from pydub import AudioSegment
import warnings
warnings.filterwarnings('ignore')

print("✅ Libraries imported successfully!")

# ============================================================================
# STEP 3: Load AI Models
# ============================================================================

print("🤖 Loading AI models...")

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # Downloads automatically
recognizer = sr.Recognizer()

print(f"✅ YOLOv8 loaded! Can detect {len(model.names)} object classes")
print("✅ Speech recognition ready!")

# ============================================================================
# STEP 4: Detection Functions
# ============================================================================

def detect_restricted_content(video_path, progress=gr.Progress()):
    """Main function to detect restricted content in videos"""
    results = []
    
    try:
        progress(0.1, desc="🔊 Extracting audio...")
        
        # Analyze audio
        audio_results = analyze_audio(video_path)
        results.extend(audio_results)
        
        progress(0.5, desc="👁️ Analyzing video frames...")
        
        # Analyze video frames
        video_results = analyze_video_frames(video_path)
        results.extend(video_results)
        
        progress(1.0, desc="✅ Analysis complete!")
        
        # Format results
        if not results:
            return "✅ **No restricted content detected!**\n\n🎉 This video appears to be clean."
        else:
            result_text = "⚠️ **Restricted Content Detected:**\n\n"
            for i, result in enumerate(results, 1):
                result_text += f"{i}. {result}\n"
            return result_text
            
    except Exception as e:
        return f"❌ **Error during analysis:** {str(e)}"

def analyze_audio(video_path):
    """Extract audio and detect profanity"""
    results = []
    
    try:
        # Create temporary files
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            audio_path = temp_audio.name
        
        # Extract audio using ffmpeg
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, acodec='pcm_s16le', ac=1, ar='16000')
            .overwrite_output()
            .run(quiet=True)
        )
        
        # Convert for speech recognition
        sound = AudioSegment.from_file(audio_path)
        
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_converted:
            converted_path = temp_converted.name
            
        sound.export(converted_path, format="wav")
        
        # Transcribe audio
        try:
            with sr.AudioFile(converted_path) as source:
                audio = recognizer.record(source)
            text = recognizer.recognize_google(audio).lower()
            
            # Check for profanity
            bad_words = [
                "damn", "hell", "shit", "fuck", "fucking", "bitch", "bastard", 
                "asshole", "dick", "piss", "crap", "pussy", "cock", "slut", 
                "whore", "violence", "kill", "murder", "rape", "terrorist"
            ]
            
            flagged_words = [word for word in bad_words if word in text]
            
            if flagged_words:
                results.append(f"🎤 **Profanity detected:** {', '.join(flagged_words)}")
                results.append(f"📝 **Text sample:** '{text[:100]}...'")
                
        except sr.UnknownValueError:
            results.append("⚠️ **Audio unclear** - Could not transcribe speech")
        except sr.RequestError as e:
            results.append(f"⚠️ **Speech recognition error:** {e}")
        
        # Cleanup
        try:
            os.unlink(audio_path)
            os.unlink(converted_path)
        except:
            pass
            
    except Exception as e:
        results.append(f"⚠️ **Audio analysis error:** {str(e)}")
    
    return results

def analyze_video_frames(video_path):
    """Analyze video frames for violent objects"""
    results = []
    
    try:
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            return ["⚠️ **Error:** Could not open video file"]
        
        frame_count = 0
        detected_objects = []
        
        # Process every 30th frame
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            frame_count += 1
            if frame_count % 30 != 0:
                continue
            
            # Run YOLO inference
            detections = model(frame, verbose=False)
            
            # Check for violent objects
            if detections[0].boxes is not None and len(detections[0].boxes) > 0:
                for box in detections[0].boxes:
                    class_id = int(box.cls[0])
                    class_name = model.names[class_id]
                    confidence = float(box.conf[0])
                    
                    # Look for potentially violent objects
                    violent_objects = ['knife', 'gun', 'rifle', 'pistol', 'weapon', 'scissors']
                    
                    if class_name.lower() in violent_objects and confidence > 0.3:
                        detected_objects.append({
                            'object': class_name,
                            'confidence': confidence,
                            'frame': frame_count
                        })
        
        cap.release()
        
        if detected_objects:
            for obj in detected_objects:
                results.append(
                    f"👁️ **Violent object:** {obj['object']} "
                    f"(confidence: {obj['confidence']:.2f}) at frame {obj['frame']}"
                )
        
    except Exception as e:
        results.append(f"⚠️ **Video analysis error:** {str(e)}")
    
    return results

print("✅ Detection functions ready!")

# ============================================================================
# STEP 5: Create Web Interface
# ============================================================================

print("🌐 Creating web interface...")

def create_interface():
    """Create Gradio web interface"""
    with gr.Blocks(
        theme=gr.themes.Soft(),
        title="Restricted Content Detection"
    ) as iface:
        
        gr.Markdown(
            """
            # 🚫 Restricted Content Detection
            
            Upload a video to analyze for restricted content:
            - 🎤 **Audio Analysis**: Detects profanity in speech
            - 👁️ **Video Analysis**: Identifies violent objects
            
            **Supported formats:** MP4, AVI, MOV, MKV, etc.
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                video_input = gr.Video(
                    label="📹 Upload Video",
                    height=300
                )
                
                analyze_btn = gr.Button(
                    "🔍 Analyze Content",
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=1):
                results_output = gr.Markdown(
                    label="📊 Analysis Results",
                    value="Upload a video and click 'Analyze Content' to see results."
                )
        
        gr.Markdown(
            """
            ---
            
            ## 💡 Tips:
            - **File size:** Smaller files process faster (recommended < 50MB)
            - **Duration:** Videos under 2 minutes work best in Colab
            - **Quality:** Clear audio improves speech recognition
            - **Internet:** Speech recognition requires internet connection
            
            ## 🔧 What gets detected:
            - **Audio:** Profanity, offensive language
            - **Video:** Weapons, knives, violent objects
            """
        )
        
        # Connect button to function
        analyze_btn.click(
            fn=detect_restricted_content,
            inputs=[video_input],
            outputs=[results_output]
        )
    
    return iface

print("✅ Interface created!")

# ============================================================================
# STEP 6: Launch Application
# ============================================================================

print("🚀 Launching Restricted Content Detection App...")
print("📱 The interface will appear below!")
print("🔗 You'll get a public URL to share!")
print("")

# Create and launch interface
app = create_interface()

# Launch with public link
app.launch(
    share=True,  # Creates a public URL
    debug=False,
    show_error=True,
    height=800
)

print("")
print("🎉 App is now running!")
print("📋 Instructions:")
print("1. Upload a video file")
print("2. Click 'Analyze Content'")
print("3. Wait for processing (30-60 seconds)")
print("4. Review the results!")
print("")
print("⚠️  Note: This Colab session will timeout after ~12 hours of inactivity")