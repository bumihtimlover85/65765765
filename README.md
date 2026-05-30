# Minimal Python Application with CI

A minimal Python application with GitHub Actions CI/CD pipeline for unit testing and integration testing.

## Project Structure

```
├── src/
│   └── myapp/
│       ├── __init__.py    # Main calculator functions and class
│       └── main.py        # Demo application
├── tests/
│   ├── test_unit.py       # Unit tests
│   └── test_integration.py # Integration tests
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI workflow
├── setup.py               # Package setup
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## Features

- Basic arithmetic functions (add, subtract, multiply, divide)
- Calculator class with history tracking
- Comprehensive unit tests
- Integration tests for complete workflows
- GitHub Actions CI/CD pipeline

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bumihtimlover85/65765765.git
   cd 65765765
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   pip install -r requirements.txt
   ```

## Running Tests

### Unit Tests
```bash
pytest tests/test_unit.py -v
```

### Integration Tests
```bash
pytest tests/test_integration.py -v
```

### All Tests
```bash
pytest tests/ -v
```

## GitHub Actions CI

The project includes a GitHub Actions CI workflow that runs on:
- Every push to `main` or `feature/*` branches
- Every pull request to `main` branch

### CI Pipeline

1. **Environment Setup**: Tests across multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12)
2. **Dependency Installation**: Installs project dependencies
3. **Unit Testing**: Runs unit tests
4. **Integration Testing**: Runs integration tests
5. **Full Test Suite**: Runs all tests together

### CI Status

[![CI](https://github.com/bumihtimlover85/65765765/actions/workflows/ci.yml/badge.svg)](https://github.com/bumihtimlover85/65765765/actions/workflows/ci.yml)

## Development

### Adding New Tests

1. **Unit Tests**: Add to `tests/test_unit.py`
   - Test individual functions and methods
   - Use descriptive test names
   - Test edge cases and error conditions

2. **Integration Tests**: Add to `tests/test_integration.py`
   - Test complete workflows
   - Test interactions between components
   - Test application behavior

### Code Quality

- Follow PEP 8 style guidelines
- Write docstrings for public functions and classes
- Keep functions small and focused
- Use meaningful variable and function names

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Commit your changes
7. Push to the branch
8. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
