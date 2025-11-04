# Contributing to FastAPI Boilerplate

Thank you for your interest in contributing! Here are some guidelines to help you get started.

## Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file based on `.env.example`

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Format code with Black: `black app/ tests/`
- Check linting with flake8: `flake8 app/`
- Type check with mypy: `mypy app/`

## Testing

- Write tests for new features
- Ensure all tests pass: `pytest`
- Maintain test coverage above 80%
- Run tests with coverage: `pytest --cov=app tests/`

## Commit Messages

- Use clear and descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Reference issues when applicable

## Pull Requests

1. Create a new branch for your feature
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
5. Update documentation if needed
6. Submit a pull request with a clear description

## Code Review Process

- All submissions require review
- Address feedback promptly
- Keep discussions focused and professional

## Questions?

Feel free to open an issue for questions or discussions.
