const { app, BrowserWindow, ipcMain, Menu } = require('electron');
const path = require('path');
const isDev = require('electron-is-dev');
const FileMonitor = require('../services/file_monitor');
const CodeAnalyzer = require('../backend/analyzer');
const AIEngine = require('../backend/ai_engine');
const LanguageDetector = require('../backend/language_detector');

let mainWindow;
let fileMonitor;
let codeAnalyzer;
let aiEngine;
let languageDetector;

const createWindow = () => {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false
    },
    icon: path.join(__dirname, '../../assets/icon.png')
  });

  const startUrl = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../../build/index.html')}`;

  mainWindow.loadURL(startUrl);

  if (isDev) {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
    if (fileMonitor) fileMonitor.stop();
  });
};

const initializeServices = () => {
  const configPath = path.join(__dirname, '../config/api.config.json');
  const config = require(configPath);

  codeAnalyzer = new CodeAnalyzer();
  languageDetector = new LanguageDetector();
  aiEngine = new AIEngine(config);
  fileMonitor = new FileMonitor();

  // Start file monitoring
  fileMonitor.on('file-change', async (filePath, code) => {
    try {
      // Detect language
      const language = languageDetector.detect(code, filePath);

      // Analyze code
      const syntaxErrors = codeAnalyzer.checkSyntax(code, language);
      const logicIssues = codeAnalyzer.checkLogic(code, language);

      // Get AI suggestions
      const suggestions = await aiEngine.getSuggestions(code, language, [
        ...syntaxErrors,
        ...logicIssues
      ]);

      // Send to renderer
      if (mainWindow && mainWindow.webContents) {
        mainWindow.webContents.send('code-analysis-result', {
          filePath,
          language,
          errors: {
            syntax: syntaxErrors,
            logic: logicIssues
          },
          suggestions,
          timestamp: new Date().toISOString()
        });
      }
    } catch (error) {
      console.error('Analysis error:', error);
      if (mainWindow && mainWindow.webContents) {
        mainWindow.webContents.send('analysis-error', {
          message: error.message,
          filePath
        });
      }
    }
  });

  fileMonitor.start();
};

// IPC Handlers
ipcMain.handle('get-config', () => {
  const configPath = path.join(__dirname, '../config/api.config.json');
  return require(configPath);
});

ipcMain.handle('update-config', (event, config) => {
  const configPath = path.join(__dirname, '../config/api.config.json');
  const fs = require('fs');
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
  return { success: true };
});

ipcMain.handle('analyze-code', async (event, { code, filename }) => {
  try {
    const language = languageDetector.detect(code, filename);
    const syntaxErrors = codeAnalyzer.checkSyntax(code, language);
    const logicIssues = codeAnalyzer.checkLogic(code, language);
    const suggestions = await aiEngine.getSuggestions(code, language, [
      ...syntaxErrors,
      ...logicIssues
    ]);

    return {
      success: true,
      language,
      errors: {
        syntax: syntaxErrors,
        logic: logicIssues
      },
      suggestions,
      totalIssues: syntaxErrors.length + logicIssues.length
    };
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
});

ipcMain.handle('get-languages', () => {
  return languageDetector.getSupportedLanguages();
});

const createMenu = () => {
  const template = [
    {
      label: 'File',
      submenu: [
        {
          label: 'Exit',
          accelerator: 'CmdOrCtrl+Q',
          click: () => {
            app.quit();
          }
        }
      ]
    },
    {
      label: 'View',
      submenu: [
        { role: 'reload' },
        { role: 'forceReload' },
        { role: 'toggleDevTools' }
      ]
    },
    {
      label: 'Help',
      submenu: [
        {
          label: 'About',
          click: () => {
            // Show about dialog
          }
        }
      ]
    }
  ];

  const menu = Menu.buildFromTemplate(template);
  Menu.setApplicationMenu(menu);
};

app.on('ready', () => {
  createWindow();
  createMenu();
  initializeServices();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
