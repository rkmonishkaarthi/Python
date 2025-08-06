# 🚫 Restricted Content Detection - Setup Guide

This is an AI-powered web application that detects **restricted content** in videos, including **profanity in audio** and **potentially violent objects** in video frames.

## 🎯 What This Application Does

- **Audio Analysis**: Extracts audio from videos and transcribes it using Google Speech Recognition to detect profane language
- **Video Analysis**: Uses YOLOv8 object detection to identify potentially violent objects (weapons, knives, etc.)
- **Web Interface**: Simple Flask web interface for uploading and analyzing videos
- **Real-time Results**: Shows detection results with confidence scores

## 📋 Prerequisites

- **Python 3.13+** (already installed ✅)
- **ffmpeg** (already installed ✅)
- **Virtual environment support** (already installed ✅)
- **Internet connection** (required for Google Speech API and YOLO model downloads)

## 🚀 Quick Start

### 1. The environment is already set up! You can start the application directly:

```bash
./start_app.sh
```

### 2. Open your web browser and go to:
```
http://localhost:5000
```

### 3. Upload a video file and click "Upload & Analyze"

## 📁 Project Structure

```
workspace/
├── app.py              # Flask web application
├── main.py             # Core detection logic
├── requirements.txt    # Python dependencies
├── start_app.sh       # Startup script
├── templates/          # HTML templates
│   ├── index.html     # Upload page
│   └── result.html    # Results page
├── uploads/           # Temporary video storage
└── venv/             # Python virtual environment
```

## 🛠️ Manual Setup (if needed)

If you need to recreate the environment:

```bash
# 1. Install system dependencies
sudo apt update
sudo apt install -y python3.13-venv python3-full ffmpeg

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install Python packages
pip install -r requirements.txt

# 5. Create uploads directory
mkdir -p uploads

# 6. Start the application
python app.py
```

## 🔧 Technical Details

### AI Models Used
- **YOLOv8n**: Pre-trained object detection model (downloads automatically)
- **Google Speech Recognition**: Cloud-based speech-to-text service

### Detection Features
- **Profanity Detection**: Scans audio transcription for offensive language
- **Object Detection**: Identifies potentially violent objects in video frames
- **Frame Sampling**: Processes every 30th frame for efficiency
- **Confidence Scoring**: Only reports detections above confidence thresholds

### File Support
- **Video Formats**: MP4, AVI, MOV, MKV, and other common formats
- **Audio Extraction**: Automatically converts to WAV format for speech recognition

## 🔍 Usage Tips

1. **Video Quality**: Higher quality videos give better detection results
2. **Audio Clarity**: Clear audio improves speech recognition accuracy
3. **File Size**: Larger files take longer to process
4. **Internet Required**: Speech recognition requires internet connection

## 🚨 Important Notes

- **Privacy**: Videos are temporarily stored locally and automatically cleaned up
- **Google API**: Speech recognition uses Google's free API (rate limits may apply)
- **Object Detection**: Currently detects weapons/knives, not custom violence patterns
- **Accuracy**: Detection accuracy depends on video/audio quality

## 🐛 Troubleshooting

### Application won't start:
```bash
# Check if virtual environment exists
ls -la venv/

# Recreate if needed
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Video upload fails:
- Check video file format (should be common video format)
- Ensure uploads/ directory exists
- Check file permissions

### Speech recognition fails:
- Ensure internet connection
- Check if audio contains speech
- Google API may have rate limits

### Object detection errors:
- YOLO model downloads automatically on first run
- Ensure sufficient disk space for model (~6MB)

## 📞 Support

If you encounter issues:
1. Check the terminal output for error messages
2. Ensure all dependencies are installed
3. Verify internet connection for cloud services
4. Check file permissions and disk space

## 🔄 Stopping the Application

Press `Ctrl+C` in the terminal where the app is running, or close the terminal window.

---

**Ready to use!** 🎉 The application is configured and ready to detect restricted content in your videos.