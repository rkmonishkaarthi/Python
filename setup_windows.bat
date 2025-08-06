@echo off
echo 🚫 Restricted Content Detection - Windows Setup
echo.
echo This script will set up the environment for the AI video content detection app
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Check if ffmpeg is available (optional, will provide instructions if not found)
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ⚠️  FFmpeg not found in PATH
    echo FFmpeg is required for video processing. You have two options:
    echo.
    echo Option 1 - Install via package manager:
    echo   - Install Chocolatey: https://chocolatey.org/install
    echo   - Run: choco install ffmpeg
    echo.
    echo Option 2 - Manual installation:
    echo   - Download from: https://ffmpeg.org/download.html#build-windows
    echo   - Extract to a folder like C:\ffmpeg
    echo   - Add C:\ffmpeg\bin to your System PATH
    echo.
    echo Would you like to continue setup without ffmpeg? (y/N)
    set /p continue="Press y to continue or any other key to exit: "
    if /i not "%continue%"=="y" (
        echo Setup cancelled. Please install ffmpeg first.
        pause
        exit /b 1
    )
) else (
    echo ✅ FFmpeg found
)

echo.
echo 📦 Setting up Python virtual environment...

REM Create virtual environment
if exist "venv" (
    echo Virtual environment already exists, removing old one...
    rmdir /s /q venv
)

python -m venv venv
if errorlevel 1 (
    echo ❌ Failed to create virtual environment
    echo Make sure you have Python 3.8+ with venv module
    pause
    exit /b 1
)

echo ✅ Virtual environment created

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
echo 📦 Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements (try Windows-specific first, fallback to general)
echo 📦 Installing Python packages (this may take a few minutes)...
if exist "requirements_windows.txt" (
    pip install -r requirements_windows.txt
) else (
    pip install -r requirements.txt
)
if errorlevel 1 (
    echo ❌ Failed to install requirements
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo ✅ Python packages installed successfully

REM Create uploads directory
if not exist "uploads" (
    mkdir uploads
    echo ✅ Created uploads directory
)

echo.
echo 🎉 Setup completed successfully!
echo.
echo To start the application:
echo   1. Double-click start_app.bat
echo   2. Or run: start_app.bat from command prompt
echo.
echo The app will be available at: http://localhost:5000
echo.
pause