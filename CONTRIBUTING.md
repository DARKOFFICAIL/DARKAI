# Contributing to DARKAI

## Code of Conduct

Please be respectful and inclusive. We want everyone to feel welcome.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported
2. If not, create a new issue with:
   - Clear title
   - Detailed description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots/logs if helpful

### Suggesting Features

1. Check if the feature has been suggested
2. Create an issue describing:
   - The feature
   - Why it's needed
   - Possible implementation

### Pull Requests

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Make your changes
4. Commit with clear messages:
   ```bash
   git commit -m 'Add amazing feature'
   ```
5. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
6. Open a Pull Request

## Development Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   pip install -r requirements.txt
   ```
3. Set up API config:
   ```bash
   cp src/config/.env.example .env
   ```
4. Run in development:
   ```bash
   npm run dev
   ```

## Coding Standards

- Use consistent indentation (2 spaces for JS, 4 for Python)
- Add comments for complex logic
- Follow existing code style
- Use meaningful variable names
- Add tests for new features

## Commit Messages

- Start with a verb (Add, Fix, Update, etc.)
- Be descriptive but concise
- Reference issues if applicable: `Fixes #123`

## Thank You!

Your contributions make DARKAI better!
