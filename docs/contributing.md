# Contributing to SCRAPINGAI

Thank you for your interest in contributing to SCRAPINGAI! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## How to Contribute

There are many ways to contribute to SCRAPINGAI:

1. **Reporting bugs**: If you find a bug, please create an issue with a detailed description of how to reproduce it.
2. **Suggesting enhancements**: If you have ideas for new features or improvements, please create an issue to discuss them.
3. **Submitting pull requests**: If you've fixed a bug or implemented a new feature, you can submit a pull request.
4. **Improving documentation**: Help us improve our documentation by fixing errors or adding examples.
5. **Answering questions**: Help other users by answering their questions in issues or discussions.

## Development Setup

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/SCRAPINGAI.git
   cd SCRAPINGAI
   ```
3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
4. Create a branch for your changes:
   ```bash
   git checkout -b feature-or-bugfix-name
   ```

## Pull Request Process

1. Ensure your code follows the project's style guidelines.
2. Add or update tests as necessary.
3. Update the documentation as needed.
4. Make sure all tests pass.
5. Submit a pull request with a clear description of the changes.

## Testing

Run the tests with pytest:

```bash
pytest
```

For test coverage:

```bash
pytest --cov=scraping_tools
```

## Code Style

We follow PEP 8 style guidelines for Python code. Please ensure your code is formatted accordingly.

You can use tools like `black` and `flake8` to check and format your code:

```bash
black .
flake8
```

## Documentation

We use MkDocs for documentation. To build and view the documentation locally:

```bash
mkdocs serve
```

Then visit `http://localhost:8000` in your browser.

## Versioning

We use [Semantic Versioning](https://semver.org/) for releases.

## License

By contributing to SCRAPINGAI, you agree that your contributions will be licensed under the project's MIT License.