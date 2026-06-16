import React from 'react';
import './Dashboard.css';

const Dashboard = ({ results = [], config = null }) => {
  const totalIssues = results.reduce((sum, r) => sum + (r.totalIssues || 0), 0);
  const languagesUsed = new Set(results.map(r => r.language)).size;
  const filesAnalyzed = results.length;

  return (
    <div className="dashboard">
      <section className="stats">
        <div className="stat-card">
          <h3>Files Analyzed</h3>
          <p className="stat-value">{filesAnalyzed}</p>
        </div>
        <div className="stat-card">
          <h3>Total Issues</h3>
          <p className="stat-value">{totalIssues}</p>
        </div>
        <div className="stat-card">
          <h3>Languages Detected</h3>
          <p className="stat-value">{languagesUsed}</p>
        </div>
        <div className="stat-card">
          <h3>API Status</h3>
          <p className="stat-value">{
            config?.apiKey && config.apiKey !== 'your-api-key-here' ? '✅' : '❌'
          }</p>
        </div>
      </section>

      <section className="recent-analysis">
        <h2>Recent Analyses</h2>
        <div className="analysis-list">
          {results.length === 0 ? (
            <div className="empty-state">
              <p>No analyses yet. Open a code file to get started!</p>
            </div>
          ) : (
            results.slice(0, 10).map((result) => (
              <div key={result.id} className="analysis-item">
                <div className="file-info">
                  <p className="file-name">{result.filePath}</p>
                  <span className="language-tag">{result.language}</span>
                </div>
                <div className="issues-info">
                  <span className="issue-count">
                    {result.totalIssues} issues
                  </span>
                  <span className="timestamp">
                    {new Date(result.timestamp).toLocaleTimeString()}
                  </span>
                </div>
              </div>
            ))
          )}
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
