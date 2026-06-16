#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Engine Module
Handles AI-powered code analysis
"""

import requests
import json
import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class AIEngine:
    """AI-powered code analysis engine"""
    
    def __init__(self, config: Dict):
        """
        Initialize AI Engine
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.api_provider = config.get('apiProvider', 'openai')
        self.api_key = config.get('apiKey')
        self.model = config.get('model', 'gpt-4')
        self.base_url = config.get('baseUrl')
        self.timeout = config.get('timeout', 30000)
        self.max_retries = config.get('retries', 3)
    
    def get_suggestions(self, code: str, language: str, errors: List = None) -> List[str]:
        """
        Get AI suggestions for code improvements
        
        Args:
            code (str): Source code
            language (str): Programming language
            errors (list): List of detected errors
            
        Returns:
            list: AI suggestions
        """
        if not self.api_key:
            logger.warning("API key not configured")
            return []
        
        try:
            if self.api_provider.lower() == 'openai':
                return self._get_openai_suggestions(code, language, errors)
            else:
                logger.warning(f"Unknown API provider: {self.api_provider}")
                return []
        except Exception as e:
            logger.error(f"Error getting AI suggestions: {e}")
            return []
    
    def _get_openai_suggestions(self, code: str, language: str, errors: List = None) -> List[str]:
        """
        Get suggestions from OpenAI API
        """
        try:
            prompt = self._build_prompt(code, language, errors)
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'model': self.model,
                'messages': [
                    {'role': 'system', 'content': 'You are a helpful code review assistant.'},
                    {'role': 'user', 'content': prompt}
                ],
                'temperature': self.config.get('temperature', 0.7),
                'max_tokens': self.config.get('maxTokens', 2000)
            }
            
            response = requests.post(
                f'{self.base_url}/chat/completions',
                headers=headers,
                json=payload,
                timeout=self.timeout / 1000
            )
            
            if response.status_code == 200:
                data = response.json()
                message = data['choices'][0]['message']['content']
                return [message]
            else:
                logger.error(f"API error: {response.status_code}")
                return []
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return []
    
    def _build_prompt(self, code: str, language: str, errors: List = None) -> str:
        """
        Build prompt for AI analysis
        """
        error_text = ""
        if errors:
            error_text = f"\n\nDetected errors:\n{json.dumps(errors, indent=2)}"
        
        prompt = f"""
Please review the following {language} code and provide:
1. Any bugs or errors found
2. Suggestions for improvement
3. Performance optimizations
4. Best practices

Code:
```{language}
{code}
```
{error_text}

Provide a concise, practical review.
        """
        return prompt
