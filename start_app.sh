#!/bin/bash

echo "🚀 Starting Restricted Content Detection App..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Create uploads directory if it doesn't exist
mkdir -p uploads

# Start the Flask application
echo "📡 Starting Flask server on http://localhost:5000"
echo "🔍 Press Ctrl+C to stop the server"
echo ""

python app.py