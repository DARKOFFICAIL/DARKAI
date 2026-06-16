#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DARKAI Startup Script
Initialize and start the bot
"""

import os
import sys
import json
from pathlib import Path


def check_dependencies():
    """Check if all dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    try:
        import flask
        import flask_cors
        import dotenv
        print("✅ All Python dependencies found")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\n📦 Please install dependencies:")
        print("   pip install -r requirements.txt")
        return False


def check_config():
    """Check if configuration file exists"""
    config_path = Path(__file__).parent / 'config' / 'api.config.json'
    
    if not config_path.exists():
        print("❌ Configuration file not found!")
        print(f"   Expected: {config_path}")
        return False
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    if config.get('apiKey') == 'your-api-key-here':
        print("⚠️  API Key not configured!")
        print(f"   Edit: {config_path}")
        print("   Add your API key to continue")
        return False
    
    print("✅ Configuration OK")
    return True


def start_backend():
    """Start the backend server"""
    print("\n🚀 Starting DARKAI Backend...")
    os.system("cd backend && python server.py")


if __name__ == '__main__':
    print("""  
    ██████╗  █████╗ ██████╗ ██╗  ██╗ █████╗ ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██║
    ██║  ██║███████║██████╔╝█████╔╝ ███████║██║
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██║
    ██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
    
    AI Code Assistant Bot v1.0.0
    """)
    
    if not check_dependencies():
        sys.exit(1)
    
    if not check_config():
        sys.exit(1)
    
    start_backend()
