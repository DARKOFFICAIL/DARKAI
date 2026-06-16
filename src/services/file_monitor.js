const chokidar = require('chokidar');
const path = require('path');
const fs = require('fs');
const { EventEmitter } = require('events');

class FileMonitor extends EventEmitter {
  constructor() {
    super();
    this.watcher = null;
    this.watchedFiles = new Map();
    this.debounceTimers = new Map();
    this.debounceDelay = 500; // milliseconds
  }

  start(directories = null) {
    try {
      // Default to monitoring documents and desktop
      const watchDirs = directories || [
        path.join(process.env.HOME || process.env.USERPROFILE, 'Documents'),
        path.join(process.env.HOME || process.env.USERPROFILE, 'Desktop')
      ].filter(dir => fs.existsSync(dir));

      const supportedExtensions = [
        '.py', '.js', '.ts', '.tsx', '.jsx',
        '.java', '.c', '.cpp', '.cc', '.cs',
        '.php', '.rb', '.go', '.rs', '.kt',
        '.swift', '.m', '.scala', '.hs', '.r'
      ];

      this.watcher = chokidar.watch(watchDirs, {
        ignored: /(^|[\\\/])\.|node_modules/,
        persistent: true,
        awaitWriteFinish: {
          stabilityThreshold: 300,
          pollInterval: 100
        }
      });

      this.watcher
        .on('change', (filePath) => this.handleFileChange(filePath))
        .on('add', (filePath) => this.handleFileChange(filePath))
        .on('error', (error) => {
          console.error('File monitor error:', error);
          this.emit('error', error);
        });

      console.log('File monitor started:', watchDirs);
    } catch (error) {
      console.error('Failed to start file monitor:', error);
      this.emit('error', error);
    }
  }

  handleFileChange(filePath) {
    // Check if file has supported extension
    const ext = path.extname(filePath).toLowerCase();
    const supportedExtensions = [
      '.py', '.js', '.ts', '.tsx', '.jsx',
      '.java', '.c', '.cpp', '.cc', '.cs',
      '.php', '.rb', '.go', '.rs', '.kt',
      '.swift', '.m', '.scala', '.hs', '.r'
    ];

    if (!supportedExtensions.includes(ext)) return;

    // Debounce file changes
    if (this.debounceTimers.has(filePath)) {
      clearTimeout(this.debounceTimers.get(filePath));
    }

    const timer = setTimeout(() => {
      try {
        const content = fs.readFileSync(filePath, 'utf-8');
        this.emit('file-change', filePath, content);
        this.watchedFiles.set(filePath, content);
      } catch (error) {
        console.error(`Error reading file ${filePath}:`, error);
      }
      this.debounceTimers.delete(filePath);
    }, this.debounceDelay);

    this.debounceTimers.set(filePath, timer);
  }

  stop() {
    if (this.watcher) {
      this.watcher.close();
      console.log('File monitor stopped');
    }
    this.debounceTimers.forEach(timer => clearTimeout(timer));
    this.debounceTimers.clear();
  }

  getWatchedFiles() {
    return Array.from(this.watchedFiles.keys());
  }
}

module.exports = FileMonitor;
