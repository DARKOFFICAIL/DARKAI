#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Analyzer Module
Handles syntax and logic checking
"""

import ast
import re
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class CodeAnalyzer:
    """Analyzes code for errors and issues"""

    def __init__(self):
        self.syntax_checkers = {
            'python': self._check_python_syntax,
            'javascript': self._check_javascript_syntax,
            'typescript': self._check_javascript_syntax,
            'java': self._check_java_syntax,
            'c': self._check_c_syntax,
            'cpp': self._check_cpp_syntax,
        }

    def check_syntax(self, code: str, language: str) -> List[Dict[str, Any]]:
        """
        Check for syntax errors

        Args:
            code (str): Source code
            language (str): Programming language

        Returns:
            list: List of syntax errors
        """
        try:
            checker = self.syntax_checkers.get(language, lambda x: [])
            return checker(code)
        except Exception as e:
            logger.error(f"Syntax check error: {e}")
            return []

    def check_logic(self, code: str, language: str) -> List[Dict[str, Any]]:
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

    def _check_python_syntax(self, code: str) -> List[Dict[str, Any]]:
        """Check Python syntax"""
        errors = []
        try:
            ast.parse(code)
        except SyntaxError as e:
            errors.append({
                'type': 'SyntaxError',
                'line': e.lineno,
                'column': e.offset,
                'message': e.msg,
                'text': e.text,
                'severity': 'error'
            })
        except IndentationError as e:
            errors.append({
                'type': 'IndentationError',
                'line': e.lineno,
                'message': e.msg,
                'severity': 'error'
            })
        return errors

    def _check_javascript_syntax(self, code: str) -> List[Dict[str, Any]]:
        """Check JavaScript/TypeScript syntax (basic)"""
        errors = []
        # Basic bracket/parenthesis matching
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        line_num = 1

        for i, char in enumerate(code):
            if char == '\n':
                line_num += 1
            elif char in brackets:
                stack.append((char, line_num))
            elif char in brackets.values():
                if not stack:
                    errors.append({
                        'type': 'SyntaxError',
                        'message': f'Unexpected closing bracket: {char}',
                        'line': line_num,
                        'severity': 'error'
                    })
                else:
                    opening = stack.pop()[0]
                    if brackets[opening] != char:
                        errors.append({
                            'type': 'SyntaxError',
                            'message': f'Mismatched brackets: {opening} and {char}',
                            'line': line_num,
                            'severity': 'error'
                        })

        for bracket, line in stack:
            errors.append({
                'type': 'SyntaxError',
                'message': f'Unclosed bracket: {bracket}',
                'line': line,
                'severity': 'error'
            })

        return errors

    def _check_java_syntax(self, code: str) -> List[Dict[str, Any]]:
        """Check Java syntax (basic)"""
        return self._check_javascript_syntax(code)  # Bracket matching

    def _check_c_syntax(self, code: str) -> List[Dict[str, Any]]:
        """Check C syntax (basic)"""
        return self._check_javascript_syntax(code)  # Bracket matching

    def _check_cpp_syntax(self, code: str) -> List[Dict[str, Any]]:
        """Check C++ syntax (basic)"""
        return self._check_javascript_syntax(code)  # Bracket matching

    def _check_undefined_variables(self, code: str, language: str) -> List[Dict[str, Any]]:
        """Check for undefined variables"""
        issues = []

        if language == 'python':
            try:
                tree = ast.parse(code)
                defined_vars = set()
                used_vars = set()

                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        for arg in node.args.args:
                            defined_vars.add(arg.arg)
                    elif isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                defined_vars.add(target.id)
                    elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                        used_vars.add(node.id)
                    elif isinstance(node, ast.Import):
                        for alias in node.names:
                            defined_vars.add(alias.asname or alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        for alias in node.names:
                            defined_vars.add(alias.asname or alias.name)

                # Built-in functions/variables
                builtins = {'print', 'len', 'range', 'str', 'int', 'float', 'list', 'dict', 'set', 'True', 'False', 'None', 'Exception', 'open', 'file', 'input', 'enumerate', 'zip', 'map', 'filter', 'sum', 'min', 'max'}
                undefined = used_vars - defined_vars - builtins

                for var in undefined:
                    issues.append({
                        'type': 'NameError',
                        'message': f"Undefined variable: '{var}'",
                        'severity': 'warning'
                    })
            except:
                pass

        return issues

    def _check_common_mistakes(self, code: str, language: str) -> List[Dict[str, Any]]:
        """Check for common programming mistakes"""
        issues = []

        if language == 'python':
            # Check for 'print' without parentheses (Python 2 vs 3)
            if re.search(r'\bprint\s+[^(]', code):
                issues.append({
                    'type': 'Warning',
                    'message': 'Python 2 style print statement detected',
                    'suggestion': 'Use print() function (Python 3)',
                    'severity': 'warning'
                })

            # Check for mutable default arguments
            if re.search(r'def\s+\w+\([^)]*=\s*\[\]', code):
                issues.append({
                    'type': 'Warning',
                    'message': 'Mutable default argument (list) detected',
                    'suggestion': 'Use None as default and initialize inside function',
                    'severity': 'warning'
                })

        elif language in ['javascript', 'typescript']:
            # Check for var usage
            if re.search(r'\bvar\s+\w+', code):
                issues.append({
                    'type': 'Warning',
                    'message': 'var keyword detected',
                    'suggestion': 'Use const or let instead of var',
                    'severity': 'warning'
                })

        return issues
