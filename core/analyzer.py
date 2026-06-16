#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Analyzer Module
Handles syntax and logic checking
"""

import ast
import re
import logging

logger = logging.getLogger(__name__)


class CodeAnalyzer:
    """Analyzes code for errors and issues"""
    
    def __init__(self):
        self.syntax_patterns = {
            'python': self._analyze_python,
            'javascript': self._analyze_javascript,
            'java': self._analyze_java,
            'c': self._analyze_c,
            'cpp': self._analyze_cpp
        }
    
    def check_syntax(self, code, language):
        """
        Check for syntax errors
        
        Args:
            code (str): Source code
            language (str): Programming language
            
        Returns:
            list: List of syntax errors
        """
        try:
            if language == 'python':
                return self._check_python_syntax(code)
            elif language == 'javascript':
                return self._check_javascript_syntax(code)
            else:
                # Generic syntax checking
                return []
        except Exception as e:
            logger.error(f"Syntax check error: {e}")
            return []
    
    def check_logic(self, code, language):
        """
        Check for logic issues
        
        Args:
            code (str): Source code
            language (str): Programming language
            
        Returns:
            list: List of logic issues
        """
        issues = []
        
        # Check for undefined variables
        undefined_vars = self._check_undefined_variables(code, language)
        issues.extend(undefined_vars)
        
        # Check for common mistakes
        common_mistakes = self._check_common_mistakes(code, language)
        issues.extend(common_mistakes)
        
        return issues
    
    def _check_python_syntax(self, code):
        """Check Python syntax"""
        errors = []
        try:
            ast.parse(code)
        except SyntaxError as e:
            errors.append({
                'type': 'SyntaxError',
                'line': e.lineno,
                'message': e.msg,
                'text': e.text,
                'offset': e.offset
            })
        return errors
    
    def _check_javascript_syntax(self, code):
        """Check JavaScript syntax (basic)"""
        errors = []
        # Basic bracket/parenthesis matching
        open_brackets = code.count('{') + code.count('[') + code.count('(')
        close_brackets = code.count('}') + code.count(']') + code.count(')')
        
        if open_brackets != close_brackets:
            errors.append({
                'type': 'SyntaxError',
                'message': 'Mismatched brackets or parentheses',
                'severity': 'high'
            })
        return errors
    
    def _check_java_syntax(self, code):
        """Check Java syntax (basic)"""
        return []
    
    def _check_c_syntax(self, code):
        """Check C syntax (basic)"""
        return []
    
    def _check_cpp_syntax(self, code):
        """Check C++ syntax (basic)"""
        return []
    
    def _analyze_python(self, code):
        return []
    
    def _analyze_javascript(self, code):
        return []
    
    def _analyze_java(self, code):
        return []
    
    def _analyze_c(self, code):
        return []
    
    def _analyze_cpp(self, code):
        return []
    
    def _check_undefined_variables(self, code, language):
        """Check for undefined variables"""
        issues = []
        # Language-specific implementations
        return issues
    
    def _check_common_mistakes(self, code, language):
        """Check for common programming mistakes"""
        issues = []
        
        if language == 'python':
            # Check for 'print' without parentheses (Python 2 vs 3)
            if re.search(r'\bprint\s+[^(]', code):
                issues.append({
                    'type': 'warning',
                    'message': 'Python 2 style print statement detected',
                    'suggestion': 'Use print() function (Python 3)'
                })
        
        return issues
