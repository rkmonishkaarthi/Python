# 🚫 Restricted Content Detection - Windows Setup Guide

This is an AI-powered web application that detects **restricted content** in videos, including **profanity in audio** and **potentially violent objects** in video frames.

## 🎯 What This Application Does

- **Audio Analysis**: Extracts audio from videos and transcribes it using Google Speech Recognition to detect profane language
- **Video Analysis**: Uses YOLOv8 object detection to identify potentially violent objects (weapons, knives, etc.)
- **Web Interface**: Simple Flask web interface for uploading and analyzing videos
- **Real-time Results**: Shows detection results with confidence scores

## 📋 Prerequisites for Windows

### Required:
- **Windows 10/11** (or Windows 7/8 with updates)
- **Python 3.8+** - Download from [python.org](https://www.python.org/downloads/)
- **Internet connection** (for Google Speech API and YOLO model downloads)

### Required during Python installation:
- ✅ **IMPORTANT**: Check "Add Python to PATH" during installation
- ✅ Check "Install for all users" (recommended)

### Optional but recommended:
- **FFmpeg** - For video processing (see setup instructions below)

## 🚀 Quick Start (Automated Setup)

### Method 1: One-Click Setup (Recommended)
1. **Download or clone** this project to your computer
2. **Double-click** `setup_windows.bat`
3. Follow the prompts (it will guide you through everything)
4. When setup is complete, **double-click** `start_app.bat`
5. Open your browser and go to `http://localhost:5000`

## 🛠️ Manual Setup (If needed)

### Step 1: Install Python
1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.8 or newer
3. **IMPORTANT**: During installation, check ✅ "Add Python to PATH"
4. Verify installation:
   ```cmd
   python --version
   ```

### Step 2: Install FFmpeg (Required for video processing)

**Option A: Using Chocolatey (Recommended)**
1. Install Chocolatey from [chocolatey.org](https://chocolatey.org/install)
2. Open Command Prompt as Administrator
3. Run:
   ```cmd
   choco install ffmpeg
   ```

**Option B: Manual Installation**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html#build-windows)
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to your System PATH:
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Click "Environment Variables"
   - Under "System Variables", find and select "Path", click "Edit"
   - Click "New" and add `C:\ffmpeg\bin`
   - Click OK on all dialogs
4. Restart Command Prompt and verify:
   ```cmd
   ffmpeg -version
   ```

### Step 3: Set up the Application
1. Open Command Prompt or PowerShell
2. Navigate to the project folder:
   ```cmd
   cd path\to\your\project\folder
   ```
3. Create virtual environment:
   ```cmd
   python -m venv venv
   ```
4. Activate virtual environment:
   ```cmd
   venv\Scripts\activate
   ```
5. Install requirements:
   ```cmd
   pip install -r requirements.txt
   ```
6. Create uploads directory:
   ```cmd
   mkdir uploads
   ```

### Step 4: Start the Application
```cmd
python app.py
```

## 📁 Project Structure

```
project-folder/
├── app.py                    # Flask web application
├── main.py                   # Core detection logic
├── requirements.txt          # Python dependencies
├── setup_windows.bat         # Windows setup script
├── start_app.bat            # Windows startup script
├── WINDOWS_SETUP_GUIDE.md   # This guide
├── templates/               # HTML templates
│   ├── index.html          # Upload page
│   └── result.html         # Results page
├── uploads/                # Temporary video storage
└── venv/                  # Python virtual environment
```

## 🖥️ Running the Application

### Using Batch Files (Easiest):
- **First time**: Double-click `setup_windows.bat`
- **Every time after**: Double-click `start_app.bat`

### Using Command Line:
```cmd
# Navigate to project folder
cd path\to\your\project

# Activate virtual environment
venv\Scripts\activate

# Start application
python app.py
```

### Accessing the Web Interface:
1. Open your web browser
2. Go to: `http://localhost:5000`
3. Upload a video file and click "Upload & Analyze"

## 🔧 Technical Details

### AI Models Used
- **YOLOv8n**: Pre-trained object detection model (downloads automatically ~6MB)
- **Google Speech Recognition**: Cloud-based speech-to-text service (free tier)

### Detection Features
- **Profanity Detection**: Scans audio transcription for offensive language
- **Object Detection**: Identifies potentially violent objects in video frames
- **Frame Sampling**: Processes every 30th frame for efficiency
- **Confidence Scoring**: Only reports detections above confidence thresholds

### Supported Video Formats
- MP4, AVI, MOV, MKV, WMV, FLV
- Most common video codecs supported

## 🐛 Troubleshooting

### "Python is not recognized"
- Reinstall Python and check ✅ "Add Python to PATH"
- Or manually add Python to PATH in System Environment Variables

### "FFmpeg is not recognized"
- Install FFmpeg following the instructions above
- Restart Command Prompt after adding to PATH

### Virtual environment issues:
```cmd
# Remove old environment
rmdir /s venv

# Create new one
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### "Permission denied" errors:
- Run Command Prompt as Administrator
- Check antivirus software isn't blocking the files

### Internet connection issues:
- Speech recognition requires internet for Google API
- YOLO model downloads on first run (needs internet)

### Video upload fails:
- Check video file format (should be common format like MP4)
- Ensure `uploads` folder exists and has write permissions
- Try a smaller video file first

## 🔍 Usage Tips

1. **Video Quality**: Higher quality videos give better detection results
2. **Audio Clarity**: Clear audio improves speech recognition accuracy
3. **File Size**: Large files (>100MB) may take longer to process
4. **First Run**: YOLOv8 model downloads automatically (~6MB)

## 🚨 Important Notes

- **Privacy**: Videos are processed locally and automatically deleted after analysis
- **Internet Required**: Speech recognition uses Google's cloud API
- **Antivirus**: Some antivirus software may flag the executable files
- **Firewall**: Flask runs on port 5000 - allow if prompted

## 🔄 Stopping the Application

- Press `Ctrl+C` in the Command Prompt window
- Or simply close the Command Prompt window

## 📞 Support

If you encounter issues:

1. **Check Python installation**:
   ```cmd
   python --version
   pip --version
   ```

2. **Check FFmpeg installation**:
   ```cmd
   ffmpeg -version
   ```

3. **Reinstall dependencies**:
   ```cmd
   venv\Scripts\activate
   pip install --upgrade -r requirements.txt
   ```

4. **Check Windows version compatibility**:
   - Windows 10/11 recommended
   - Windows 7/8 may work with updates

---

## 🎉 Ready to Use!

Once setup is complete:
1. Double-click `start_app.bat`
2. Open browser to `http://localhost:5000`
3. Upload videos and analyze restricted content!

**The application is now configured for Windows and ready to detect restricted content in your videos.** 🚀