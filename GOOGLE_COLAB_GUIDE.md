# 🚫 Restricted Content Detection - Google Colab Guide

Run this AI-powered video content detection app directly in **Google Colab** - no installation required!

## 🎯 What This Does

- **🎤 Audio Analysis**: Detects profanity in video audio using Google Speech Recognition
- **👁️ Video Analysis**: Identifies violent objects (weapons, knives) using YOLOv8 
- **🌐 Web Interface**: Simple upload and analyze interface
- **☁️ Cloud-Based**: Runs entirely in Google's cloud servers

---

## 🚀 Quick Start (2 Steps!)

### Method 1: Use the Pre-Made Script

1. **Open Google Colab**: Go to [colab.research.google.com](https://colab.research.google.com)

2. **Create New Notebook**: Click "New Notebook"

3. **Copy & Paste**: Copy the entire content from `Colab_Setup.py` into a Colab cell

4. **Run**: Click the play button or press `Ctrl+Enter`

5. **Use the App**: A web interface will appear with a public URL!

### Method 2: Manual Setup (Step by Step)

If you prefer to understand each step:

#### Cell 1: Install Dependencies
```python
# Install system dependencies
!apt update -qq
!apt install -y ffmpeg

# Install Python packages
!pip install -q ultralytics opencv-python speechrecognition pydub ffmpeg-python gradio

print("✅ Dependencies installed!")
```

#### Cell 2: Import Libraries
```python
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

print("✅ Libraries imported!")
```

#### Cell 3: Load Models
```python
# Load YOLOv8 model (downloads automatically)
model = YOLO('yolov8n.pt')
recognizer = sr.Recognizer()

print(f"✅ YOLOv8 loaded! Can detect {len(model.names)} object classes")
```

#### Cell 4: Copy Detection Functions
Copy the detection functions from `Colab_Setup.py` (the large function definitions)

#### Cell 5: Launch Interface
```python
# Create and launch the web interface
app = create_interface()
app.launch(share=True, height=800)
```

---

## 📱 Using the Web Interface

### 1. **Upload Video**
- Click the video upload area
- Select your video file (MP4, AVI, MOV, etc.)
- Wait for upload to complete

### 2. **Analyze Content**
- Click "🔍 Analyze Content" button
- Progress bar shows: Audio extraction → Video analysis
- Wait 30-60 seconds for processing

### 3. **Review Results**
**If restricted content found:**
- 🎤 Profanity detected with specific words
- 👁️ Violent objects with confidence scores
- 📝 Sample transcribed text

**If content is clean:**
- ✅ "No restricted content detected" message

---

## 🔧 Technical Details

### **What Runs in Colab:**
- **YOLOv8n**: Pre-trained object detection (~6MB download)
- **Google Speech Recognition**: Cloud-based transcription
- **FFmpeg**: Video/audio processing
- **Gradio**: Web interface framework

### **Processing:**
- **Frame Sampling**: Every 30th frame for efficiency
- **Audio Extraction**: Converted to 16kHz WAV
- **Object Detection**: Scans for weapons/violent objects
- **Speech Recognition**: Transcribes and checks for profanity

### **Colab Advantages:**
- ✅ **Free GPU/CPU**: Faster processing than local machines
- ✅ **No Installation**: Everything runs in the cloud
- ✅ **Public URLs**: Share the app with others
- ✅ **Pre-installed**: Many packages already available

---

## 💡 Colab Tips & Optimization

### **For Better Performance:**
1. **Enable GPU**: Runtime → Change runtime type → GPU
2. **Smaller Videos**: Under 50MB process faster
3. **Short Duration**: Videos under 2 minutes are optimal
4. **Close Other Tabs**: Free up browser memory

### **File Upload Tips:**
- **Direct Upload**: Use the Colab file browser (left sidebar)
- **Google Drive**: Mount drive for larger files
- **URL Download**: Use `!wget` for online videos

### **Colab Limitations:**
- **Session Timeout**: ~12 hours of inactivity
- **File Storage**: Temporary (files deleted when session ends)
- **Internet Required**: For speech recognition and model downloads

---

## 🐛 Troubleshooting

### **"Package not found" errors:**
```python
# Reinstall packages
!pip install --upgrade ultralytics gradio speechrecognition
```

### **FFmpeg errors:**
```python
# Reinstall ffmpeg
!apt update && apt install -y ffmpeg
```

### **Speech recognition fails:**
- Check internet connection
- Ensure video has clear audio
- Google API rate limits may apply

### **Video upload fails:**
- Try smaller file size (< 50MB)
- Use common formats (MP4, AVI, MOV)
- Check browser console for errors

### **Session timeouts:**
- Save important results before timeout
- Re-run the setup script to restart

---

## 📂 File Management in Colab

### **Upload Videos:**
```python
# Method 1: File browser (left sidebar)
# Method 2: Code upload
from google.colab import files
uploaded = files.upload()
```

### **Download Results:**
```python
# Save results to file
with open('detection_results.txt', 'w') as f:
    f.write(results_text)

# Download file
files.download('detection_results.txt')
```

### **Mount Google Drive:**
```python
from google.colab import drive
drive.mount('/content/drive')

# Access files in drive
video_path = '/content/drive/MyDrive/videos/sample.mp4'
```

---

## 🚀 Advanced Usage

### **Batch Processing:**
```python
import glob

# Process multiple videos
video_files = glob.glob('/content/*.mp4')
results = {}

for video in video_files:
    print(f"Processing {video}...")
    result = detect_restricted_content(video)
    results[video] = result
    
print("Batch processing complete!")
```

### **Custom Profanity List:**
```python
# Modify the bad_words list in analyze_audio function
custom_bad_words = ["your", "custom", "words", "here"]
```

### **Different YOLO Models:**
```python
# Use larger model for better accuracy (slower)
model = YOLO('yolov8s.pt')  # Small
model = YOLO('yolov8m.pt')  # Medium
model = YOLO('yolov8l.pt')  # Large
```

---

## 🎉 Ready to Use!

### **Quick Checklist:**
1. ✅ Open Google Colab
2. ✅ Copy the script from `Colab_Setup.py`
3. ✅ Paste into a Colab cell
4. ✅ Run the cell
5. ✅ Upload videos and analyze!

### **What You Get:**
- 🌐 **Web Interface**: Easy drag-and-drop video upload
- 🔗 **Public URL**: Share with others (optional)
- 📊 **Detailed Results**: Profanity and object detection
- ☁️ **Cloud Processing**: Fast GPU-accelerated analysis

**Your AI-powered restricted content detection app is ready to run in Google Colab!** 🚀

---

*Note: Google Colab provides free compute resources with some limitations. For heavy usage, consider Colab Pro.*