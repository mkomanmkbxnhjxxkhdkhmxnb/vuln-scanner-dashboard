#!/bin/bash

echo "========================================"
echo "Vulnerability Scanner Dashboard"
echo "========================================"
echo ""
echo "Starting application..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run application
echo ""
echo "Starting Flask server..."
echo "Dashboard will open at: http://localhost:5000"
echo ""
python app.py
