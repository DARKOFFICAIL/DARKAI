import React, { useState } from 'react';
import './CodeAnalyzer.css';

const CodeAnalyzer = ({ config, onResult }) => {
  const [code, setCode] = useState('');
  const [filename, setFilename] = useState('example.py');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!code.trim()) {
      setError('Please enter some code to analyze');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      if (window.api && window.api.analyzeCode) {
        const result = await window.api.analyzeCode(code, filename);
        if (result.success) {
          setResults(result);
          onResult((prev) => [result, ...prev]);
        } else {
          setError(result.error || 'Analysis failed');
        }
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="analyzer">
      <div className="analyzer-form">
        <div className="form-group">
          <label>Filename:</label>
          <input
            type="text"
            value={filename}
            onChange={(e) => setFilename(e.target.value)}
            placeholder="example.py"
          />
        </div>

        <div className="form-group">
          <label>Code:</label>
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            placeholder="Paste your code here..."
            rows="15"
          />
        </div>

        <button
          onClick={handleAnalyze}
          disabled={loading}
          className="analyze-btn"
        >
          {loading ? '🔄 Analyzing...' : '🔍 Analyze Code'}
        </button>
      </div>

      {error && (
        <div className="error-message">
          <p>❌ {error}</p>
        </div>
      )}

      {results && (
        <div className="results">
          <h3>Analysis Results</h3>
          <div className="result-summary">
            <p>Language: <strong>{results.language}</strong></p>
            <p>Total Issues: <strong>{results.totalIssues}</strong></p>
          </div>

          {results.errors && results.errors.syntax && results.errors.syntax.length > 0 && (
            <div className="issues-section">
              <h4>Syntax Errors ({results.errors.syntax.length})</h4>
              {results.errors.syntax.map((err, idx) => (
                <div key={idx} className="issue">
                  <p className="error-msg">❌ {err.message}</p>
                  {err.line && <p className="line-num">Line {err.line}</p>}
                </div>
              ))}
            </div>
          )}

          {results.errors && results.errors.logic && results.errors.logic.length > 0 && (
            <div className="issues-section">
              <h4>Logic Issues ({results.errors.logic.length})</h4>
              {results.errors.logic.map((err, idx) => (
                <div key={idx} className="issue">
                  <p className="warning-msg">⚠️ {err.message}</p>
                  {err.suggestion && <p className="suggestion">💡 {err.suggestion}</p>}
                </div>
              ))}
            </div>
          )}

          {results.suggestions && results.suggestions.length > 0 && (
            <div className="suggestions-section">
              <h4>AI Suggestions</h4>
              {results.suggestions.map((suggestion, idx) => (
                <div key={idx} className="suggestion-box">
                  <p>{suggestion}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default CodeAnalyzer;
