Write-Host "🚀 Starting Restricted Content Detection App..." -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "❌ Virtual environment not found. Please run setup first." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Activate virtual environment
& "venv\Scripts\Activate.ps1"

# Create uploads directory if it doesn't exist
if (-not (Test-Path "uploads")) {
    New-Item -ItemType Directory -Path "uploads" | Out-Null
}

# Start the Flask application
Write-Host "📡 Starting Flask server on http://localhost:5000" -ForegroundColor Green
Write-Host "🔍 Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python app.py