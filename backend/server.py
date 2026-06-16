#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DARKAI Backend Server
AI-powered Code Analysis Bot
"""

import os
import json
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.analyzer import CodeAnalyzer
from core.language_detector import LanguageDetector
from core.ai_engine import AIEngine

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load API config
config_path = Path(__file__).parent.parent / 'config' / 'api.config.json'
with open(config_path, 'r') as f:
    config = json.load(f)

# Initialize components
lang_detector = LanguageDetector()
code_analyzer = CodeAnalyzer()
ai_engine = AIEngine(config)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'service': 'DARKAI Backend'
    })


@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    """
    Main endpoint for code analysis
    
    Expected JSON:
    {
        "code": "code content",
        "filename": "file.py",
        "language": "python",  # optional - auto-detect if not provided
        "context": {}  # optional additional context
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'code' not in data:
            return jsonify({'error': 'Missing code parameter'}), 400
        
        code = data['code']
        filename = data.get('filename', 'unknown')
        language = data.get('language')
        
        # Auto-detect language if not provided
        if not language:
            language = lang_detector.detect(code, filename)
        
        logger.info(f"Analyzing {language} code from {filename}")
        
        # Analyze code
        syntax_errors = code_analyzer.check_syntax(code, language)
        logic_issues = code_analyzer.check_logic(code, language)
        
        # Get AI suggestions
        ai_suggestions = ai_engine.get_suggestions(
            code=code,
            language=language,
            errors=syntax_errors + logic_issues
        )
        
        response = {
            'success': True,
            'language': language,
            'filename': filename,
            'issues': {
                'syntax_errors': syntax_errors,
                'logic_issues': logic_issues
            },
            'suggestions': ai_suggestions,
            'summary': {
                'total_issues': len(syntax_errors) + len(logic_issues),
                'severity': 'high' if syntax_errors else 'medium' if logic_issues else 'low'
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error analyzing code: {str(e)}", exc_info=True)
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/api/languages', methods=['GET'])
def get_supported_languages():
    """Get list of supported programming languages"""
    languages = lang_detector.get_supported_languages()
    return jsonify({
        'supported_languages': languages,
        'total': len(languages)
    })


@app.route('/api/config', methods=['GET'])
def get_config():
    """Get current configuration (without sensitive data)"""
    safe_config = {
        'apiProvider': config.get('apiProvider'),
        'model': config.get('model'),
        'language': config.get('language'),
        'debugMode': config.get('debugMode')
    }
    return jsonify(safe_config)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.getenv('BOT_PORT', 5000))
    debug = os.getenv('BOT_DEBUG', 'false').lower() == 'true'
    
    logger.info(f"Starting DARKAI Backend on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=debug)
