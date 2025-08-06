@echo off
echo 🚀 Starting Restricted Content Detection App...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo ❌ Virtual environment not found. Please run setup first.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Create uploads directory if it doesn't exist
if not exist "uploads" mkdir uploads

REM Start the Flask application
echo 📡 Starting Flask server on http://localhost:5000
echo 🔍 Press Ctrl+C to stop the server
echo.

python app.py