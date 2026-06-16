#!/bin/bash
# DARKAI Startup Script for Linux/macOS

echo ""
echo "██████╗  █████╗ ██████╗ ██╗  ██╗ █████╗ ██╗"
echo "██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██║"
echo "██║  ██║███████║██████╔╝█████╔╝ ███████║██║"
echo "██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██║"
echo "██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║"
echo "╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝"
echo ""
echo "AI Code Assistant Bot v1.0.0"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check dependencies
echo "🔍 Checking dependencies..."
python3 -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Start the bot
echo "🚀 Starting DARKAI Backend..."
cd backend
python3 server.py
