const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld(
  'api',
  {
    // Config operations
    getConfig: () => ipcRenderer.invoke('get-config'),
    updateConfig: (config) => ipcRenderer.invoke('update-config', config),

    // Code analysis
    analyzeCode: (code, filename) =>
      ipcRenderer.invoke('analyze-code', { code, filename }),

    // Language support
    getLanguages: () => ipcRenderer.invoke('get-languages'),

    // Listen for analysis results
    onAnalysisResult: (callback) =>
      ipcRenderer.on('code-analysis-result', (event, data) => callback(data)),

    // Listen for analysis errors
    onAnalysisError: (callback) =>
      ipcRenderer.on('analysis-error', (event, data) => callback(data)),

    // Remove listeners
    removeAnalysisResultListener: () =>
      ipcRenderer.removeAllListeners('code-analysis-result'),
    removeAnalysisErrorListener: () =>
      ipcRenderer.removeAllListeners('analysis-error')
  }
);
