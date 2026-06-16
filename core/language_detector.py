#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Language Detector Module
Automatic detection of programming language
"""

import os
from pathlib import Path


class LanguageDetector:
    """Detects programming language from code or filename"""
    
    FILE_EXTENSIONS = {
        'python': ['.py', '.pyw', '.pyx'],
        'javascript': ['.js', '.mjs', '.jsx'],
        'typescript': ['.ts', '.tsx'],
        'java': ['.java'],
        'c': ['.c'],
        'cpp': ['.cpp', '.cc', '.cxx', '.c++'],
        'csharp': ['.cs'],
        'php': ['.php', '.php3', '.php4', '.php5'],
        'ruby': ['.rb', '.ruby'],
        'go': ['.go'],
        'rust': ['.rs'],
        'kotlin': ['.kt', '.kts'],
        'swift': ['.swift'],
        'objective_c': ['.m', '.h'],
        'scala': ['.scala'],
        'haskell': ['.hs'],
        'r': ['.r', '.R'],
        'matlab': ['.m'],
        'sql': ['.sql'],
        'html': ['.html', '.htm'],
        'css': ['.css'],
        'json': ['.json'],
        'xml': ['.xml'],
        'yaml': ['.yaml', '.yml']
    }
    
    SHEBANG_MAP = {
        'python': ['python', 'python3'],
        'ruby': ['ruby'],
        'perl': ['perl'],
        'bash': ['bash', 'sh']
    }
    
    def detect(self, code, filename=None):
        """
        Detect programming language
        
        Args:
            code (str): Source code content
            filename (str): Optional filename
            
        Returns:
            str: Detected language
        """
        # Try extension-based detection first
        if filename:
            lang = self._detect_by_extension(filename)
            if lang:
                return lang
            
            # Try shebang detection
            lang = self._detect_by_shebang(code)
            if lang:
                return lang
        
        # Try content-based detection
        lang = self._detect_by_content(code)
        if lang:
            return lang
        
        return 'unknown'
    
    def _detect_by_extension(self, filename):
        """Detect language by file extension"""
        file_ext = Path(filename).suffix.lower()
        
        for language, extensions in self.FILE_EXTENSIONS.items():
            if file_ext in extensions:
                return language
        
        return None
    
    def _detect_by_shebang(self, code):
        """Detect language by shebang line"""
        if not code.startswith('#!'):
            return None
        
        shebang_line = code.split('\n')[0]
        
        for language, shebangs in self.SHEBANG_MAP.items():
            for shebang in shebangs:
                if shebang in shebang_line:
                    return language
        
        return None
    
    def _detect_by_content(self, code):
        """Detect language by content analysis"""
        code_lower = code.lower()
        
        # Python
        if 'def ' in code and 'import ' in code:
            return 'python'
        
        # JavaScript
        if 'function ' in code or 'const ' in code or 'let ' in code:
            return 'javascript'
        
        # Java
        if 'public class ' in code or 'public static void main' in code:
            return 'java'
        
        # C
        if '#include ' in code and 'int main' in code:
            return 'c'
        
        # C++
        if '#include ' in code and ('iostream' in code or 'vector' in code):
            return 'cpp'
        
        # PHP
        if '<?php' in code or '<?=' in code:
            return 'php'
        
        # Ruby
        if 'def ' in code and 'end' in code and ':' not in code:
            return 'ruby'
        
        # Go
        if 'package ' in code and 'func ' in code:
            return 'go'
        
        # Rust
        if 'fn ' in code and '::' in code:
            return 'rust'
        
        return None
    
    def get_supported_languages(self):
        """Get list of supported languages"""
        return list(self.FILE_EXTENSIONS.keys())
