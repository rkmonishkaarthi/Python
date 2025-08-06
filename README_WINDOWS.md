# 🚫 Restricted Content Detection for Windows

An AI-powered web application that detects **profanity in audio** and **violent objects in video** using machine learning.

## 🚀 Quick Start for Windows

### Prerequisites
1. **Python 3.8+** from [python.org](https://python.org) (**Check "Add to PATH"**)
2. **FFmpeg** (optional but recommended)

### One-Click Setup
1. **Download** this project folder
2. **Double-click** `setup_windows.bat` 
3. **Wait** for setup to complete
4. **Double-click** `start_app.bat`
5. **Open browser** to `http://localhost:5000`
6. **Upload a video** and analyze!

## 📂 Windows Files

- `setup_windows.bat` - First-time setup (run once)
- `start_app.bat` - Start the app (run every time)
- `start_app.ps1` - PowerShell version
- `requirements_windows.txt` - Windows-optimized packages

## 🛠️ Manual Installation

If batch files don't work:

```cmd
# 1. Open Command Prompt in project folder
# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install packages
pip install -r requirements.txt

# 5. Start app
python app.py
```

## 🎯 Features

- **🎤 Audio Analysis**: Detects profanity in video audio
- **👁️ Video Analysis**: Identifies weapons/violent objects  
- **🌐 Web Interface**: Simple upload and results page
- **⚡ Fast Processing**: Optimized for Windows performance

## 🐛 Common Windows Issues

**"Python not found"**
- Reinstall Python, check ✅ "Add to PATH"

**"FFmpeg not found"**  
- Install via Chocolatey: `choco install ffmpeg`
- Or download from [ffmpeg.org](https://ffmpeg.org)

**Antivirus blocking**
- Allow Python and the project folder in antivirus

**Permission errors**
- Run Command Prompt as Administrator

## 💡 Usage

1. **Start**: Double-click `start_app.bat`
2. **Upload**: Drop video file in browser
3. **Wait**: Processing takes 30-60 seconds
4. **Review**: Check detection results
5. **Stop**: Press Ctrl+C in command window

## 🔧 Supported Formats

- **Video**: MP4, AVI, MOV, MKV, WMV
- **Audio**: Automatic extraction from video
- **Size**: Recommended under 100MB for faster processing

---

**Ready to detect restricted content in your videos!** 🎉

For detailed instructions, see `WINDOWS_SETUP_GUIDE.md`