import React, { useState, useEffect } from 'react';
import './App.css';
import CodeAnalyzer from './components/CodeAnalyzer';
import Settings from './components/Settings';
import Dashboard from './components/Dashboard';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [config, setConfig] = useState(null);
  const [analysisResults, setAnalysisResults] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Load configuration on mount
    loadConfig();

    // Listen for analysis results
    if (window.api && window.api.onAnalysisResult) {
      window.api.onAnalysisResult((data) => {
        setAnalysisResults((prev) => [
          { ...data, id: Date.now() },
          ...prev.slice(0, 19) // Keep last 20 results
        ]);
      });
    }

    return () => {
      // Cleanup listeners
      if (window.api) {
        window.api.removeAnalysisResultListener();
        window.api.removeAnalysisErrorListener();
      }
    };
  }, []);

  const loadConfig = async () => {
    try {
      if (window.api && window.api.getConfig) {
        const cfg = await window.api.getConfig();
        setConfig(cfg);
      }
    } catch (error) {
      console.error('Failed to load config:', error);
    }
  };

  const handleUpdateConfig = async (newConfig) => {
    try {
      if (window.api && window.api.updateConfig) {
        await window.api.updateConfig(newConfig);
        setConfig(newConfig);
      }
    } catch (error) {
      console.error('Failed to update config:', error);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1>🤖 DARKAI</h1>
          <p className="subtitle">AI Code Assistant</p>
        </div>
        <nav className="nav-tabs">
          <button
            className={`tab-btn ${activeTab === 'dashboard' ? 'active' : ''}`}
            onClick={() => setActiveTab('dashboard')}
          >
            📊 Dashboard
          </button>
          <button
            className={`tab-btn ${activeTab === 'analyzer' ? 'active' : ''}`}
            onClick={() => setActiveTab('analyzer')}
          >
            🔍 Analyzer
          </button>
          <button
            className={`tab-btn ${activeTab === 'settings' ? 'active' : ''}`}
            onClick={() => setActiveTab('settings')}
          >
            ⚙️ Settings
          </button>
        </nav>
      </header>

      <main className="app-content">
        {activeTab === 'dashboard' && (
          <Dashboard results={analysisResults} config={config} />
        )}
        {activeTab === 'analyzer' && (
          <CodeAnalyzer config={config} onResult={setAnalysisResults} />
        )}
        {activeTab === 'settings' && (
          <Settings config={config} onUpdate={handleUpdateConfig} />
        )}
      </main>

      <footer className="app-footer">
        <p>DARKAI v1.0.0 | AI-Powered Code Assistant</p>
      </footer>
    </div>
  );
}

export default App;
