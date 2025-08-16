# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Test-Driven Development (TDD) educational project demonstrating TDD practices using both pytest and unittest frameworks. The project implements simple examples (Calculator) and more complex scenarios (BankAccount with custom exceptions) to show the TDD Red-Green-Refactor cycle.

## Project Architecture

The codebase follows a simple two-layer architecture:

- **`src/`**: Implementation code for business logic
  - `calculator.py`: Basic arithmetic operations with error handling
  - `bank_account.py`: Stateful account management with custom `InsufficientFundsError` exception
  
- **`tests/`**: Dual testing approach demonstrating framework differences
  - `test_*.py`: pytest implementation with simple assertions and `pytest.raises()`
  - `unittest_*.py`: unittest implementation with rich assertion methods and `assertRaises()`

Both test suites cover identical functionality to demonstrate framework patterns side-by-side.

## Development Commands

### Running Tests

**pytest (preferred for new tests):**
```bash
# All pytest tests
pytest

# Specific test file
pytest tests/test_calculator.py -v

# With coverage
pytest --cov=src
```

**unittest:**
```bash
# All unittest tests
python -m unittest discover tests -p "unittest_*.py" -v

# Specific test file
python -m unittest tests.unittest_calculator -v

# Specific test class/method
python -m unittest tests.unittest_calculator.TestCalculator.test_add_two_positive_numbers -v
```

### Setup
```bash
pip install -r requirements.txt
```

## TDD Workflow

When adding new functionality, follow the established TDD pattern:

1. **Red**: Write failing tests first in both frameworks (for educational comparison)
2. **Green**: Implement minimal code to pass tests
3. **Refactor**: Improve code while maintaining green tests

## Testing Patterns

The project demonstrates key testing patterns:
- **Setup methods**: `setup_method()` (pytest) vs `setUp()` (unittest)
- **Exception testing**: `pytest.raises()` vs `assertRaises()` context managers
- **Floating point comparisons**: Manual tolerance vs `assertAlmostEqual()`
- **Rich assertions**: Simple `assert` vs specialized unittest methods