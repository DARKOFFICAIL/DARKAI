@echo off
REM DARKAI Startup Script for Windows

echo.
echo   ██████╗  █████╗ ██████╗ ██╗  ██╗ █████╗ ██╗
echo   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██║
echo   ██║  ██║███████║██████╔╝█████╔╝ ███████║██║
echo   ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██║
echo   ██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║
echo   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
echo.
echo   AI Code Assistant Bot v1.0.0
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8 or higher.
    exit /b 1
)

echo ✅ Python found

REM Check dependencies
echo 🔍 Checking dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    exit /b 1
)

echo ✅ Dependencies installed

REM Start the bot
echo 🚀 Starting DARKAI Backend...
cd backend
python server.py
