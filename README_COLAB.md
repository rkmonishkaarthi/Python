# 🚫 Restricted Content Detection for Google Colab

**AI-powered video analysis** that detects **profanity** and **violent objects** - runs entirely in Google Colab!

## 🚀 Super Quick Start (30 seconds!)

1. **Open** [Google Colab](https://colab.research.google.com)
2. **Create** new notebook  
3. **Copy** the entire content from `Colab_Setup.py`
4. **Paste** into a Colab cell
5. **Run** the cell (Ctrl+Enter)
6. **Upload** videos and analyze! 🎉

## 🎯 What It Does

- **🎤 Audio**: Detects profanity in speech
- **👁️ Video**: Finds weapons/violent objects  
- **🌐 Interface**: Simple web upload
- **☁️ Cloud**: Runs on Google's servers (free!)

## 📱 How to Use

1. **Upload** your video (MP4, AVI, MOV, etc.)
2. **Click** "Analyze Content" 
3. **Wait** 30-60 seconds
4. **Review** detailed results

## ✨ Features

- ✅ **No Installation** - Everything in the cloud
- ✅ **Free GPU Access** - Faster than your computer
- ✅ **Public URLs** - Share with others
- ✅ **Real-time Progress** - See what's happening
- ✅ **Detailed Results** - Confidence scores and timestamps

## 🔧 What Gets Detected

**Audio Analysis:**
- Profanity and offensive language
- Clear transcription of speech

**Video Analysis:**  
- Weapons (knives, guns, etc.)
- Confidence scores for each detection
- Frame-by-frame analysis

## 💡 Pro Tips

- **Enable GPU**: Runtime → Change runtime type → GPU
- **Smaller files**: Under 50MB process faster
- **Clear audio**: Better speech recognition
- **Save results**: Download before session timeout

## 📂 Files You Need

- **`Colab_Setup.py`** - Complete setup script (copy this!)
- **`GOOGLE_COLAB_GUIDE.md`** - Detailed instructions
- **Your videos** - Upload and analyze!

## 🐛 Quick Fixes

**Packages not found?**
```python
!pip install --upgrade ultralytics gradio speechrecognition
```

**FFmpeg error?**
```python
!apt update && apt install -y ffmpeg
```

**Session timeout?**
- Re-run the setup script
- Enable GPU for better performance

## 🎉 Ready to Go!

**Perfect for:**
- Content moderators
- Video analysis projects  
- Educational demonstrations
- Quick video screening

**Your AI-powered content detection app is ready in Google Colab!** 🚀

---

*No downloads, no installation, no hassle - just paste and run!*