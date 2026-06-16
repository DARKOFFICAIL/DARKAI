import React, { useState, useEffect } from 'react';
import './Settings.css';

const Settings = ({ config, onUpdate }) => {
  const [formData, setFormData] = useState(config || {});
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    if (config) {
      setFormData(config);
    }
  }, [config]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSave = async () => {
    await onUpdate(formData);
    setSaved(true);
    setTimeout(() => setSaved(false), 3000);
  };

  return (
    <div className="settings">
      <div className="settings-form">
        <section className="settings-section">
          <h3>API Configuration</h3>
          
          <div className="form-group">
            <label>API Provider:</label>
            <select
              name="apiProvider"
              value={formData.apiProvider || 'openai'}
              onChange={handleChange}
            >
              <option value="openai">OpenAI</option>
              <option value="claude">Claude</option>
              <option value="local">Local Model</option>
            </select>
          </div>

          <div className="form-group">
            <label>API Key:</label>
            <input
              type="password"
              name="apiKey"
              value={formData.apiKey || ''}
              onChange={handleChange}
              placeholder="Enter your API key"
            />
            <small>🔒 Your API key is stored locally and never shared</small>
          </div>

          <div className="form-group">
            <label>Model:</label>
            <input
              type="text"
              name="model"
              value={formData.model || 'gpt-4'}
              onChange={handleChange}
              placeholder="gpt-4"
            />
          </div>

          <div className="form-group">
            <label>Base URL:</label>
            <input
              type="text"
              name="baseUrl"
              value={formData.baseUrl || ''}
              onChange={handleChange}
              placeholder="https://api.openai.com/v1"
            />
          </div>
        </section>

        <section className="settings-section">
          <h3>Analysis Settings</h3>

          <div className="form-group">
            <label>Temperature:</label>
            <input
              type="number"
              name="temperature"
              value={formData.temperature || 0.7}
              onChange={handleChange}
              min="0"
              max="1"
              step="0.1"
            />
            <small>Lower = more deterministic, Higher = more creative</small>
          </div>

          <div className="form-group">
            <label>Max Tokens:</label>
            <input
              type="number"
              name="maxTokens"
              value={formData.maxTokens || 2000}
              onChange={handleChange}
              min="100"
              max="4000"
            />
          </div>

          <div className="form-group">
            <label>Language:</label>
            <select
              name="language"
              value={formData.language || 'en'}
              onChange={handleChange}
            >
              <option value="en">English</option>
              <option value="ar">العربية</option>
              <option value="fr">Français</option>
              <option value="de">Deutsch</option>
              <option value="es">Español</option>
            </select>
          </div>
        </section>

        <section className="settings-section">
          <h3>General Settings</h3>

          <div className="form-group">
            <label>
              <input
                type="checkbox"
                name="enableFileMonitoring"
                checked={formData.enableFileMonitoring !== false}
                onChange={handleChange}
              />
              Enable File Monitoring
            </label>
            <small>Automatically analyze files as you edit them</small>
          </div>

          <div className="form-group">
            <label>
              <input
                type="checkbox"
                name="debugMode"
                checked={formData.debugMode || false}
                onChange={handleChange}
              />
              Debug Mode
            </label>
            <small>Show detailed logs and error information</small>
          </div>
        </section>

        <button onClick={handleSave} className="save-btn">
          💾 Save Settings
        </button>

        {saved && (
          <div className="success-message">
            ✅ Settings saved successfully!
          </div>
        )}
      </div>
    </div>
  );
};

export default Settings;
