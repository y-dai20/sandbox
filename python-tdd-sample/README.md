# Python TDD Sample Project

This project demonstrates Test-Driven Development (TDD) practices in Python using both pytest and unittest frameworks.

## What is TDD?

Test-Driven Development (TDD) is a software development methodology where you:

1. **Red**: Write a failing test first
2. **Green**: Write the minimum code to make the test pass
3. **Refactor**: Improve the code while keeping tests green

## Project Structure

```
python-tdd-sample/
├── src/
│   ├── __init__.py
│   ├── calculator.py         # Simple calculator implementation
│   └── bank_account.py       # Bank account with more complex logic
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py    # pytest version
│   ├── test_bank_account.py  # pytest version
│   ├── unittest_calculator.py    # unittest version
│   └── unittest_bank_account.py  # unittest version
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run all tests with pytest:
   ```bash
   pytest
   ```

3. Run all tests with unittest:
   ```bash
   python -m unittest discover tests -p "unittest_*.py" -v
   ```

4. Run tests with coverage:
   ```bash
   pytest --cov=src
   ```

## Examples

### Calculator (Simple TDD Example)

The `Calculator` class demonstrates basic TDD with simple mathematical operations:
- Addition, subtraction, multiplication, division
- Error handling for division by zero

### BankAccount (Complex TDD Example)

The `BankAccount` class shows more complex TDD scenarios:
- State management (balance tracking)
- Custom exceptions (`InsufficientFundsError`)
- Input validation
- Edge cases (zero amounts, exact balance withdrawals)

## TDD Process Demonstrated

1. **Write tests first** (`test_*.py` files)
   - Define expected behavior
   - Include edge cases and error conditions
   - Use descriptive test names

2. **Run tests** (they should fail initially)
   ```bash
   pytest tests/test_calculator.py -v
   ```

3. **Implement minimum code** to pass tests
   - Write just enough code to make tests green
   - Don't over-engineer

4. **Refactor** if needed while keeping tests green

## Key TDD Benefits Shown

- **Better design**: Tests force you to think about interfaces first
- **Confidence**: Comprehensive test suite catches regressions
- **Documentation**: Tests serve as living documentation
- **Debugging**: Failing tests pinpoint issues quickly

## Running Individual Test Files

### With pytest:
```bash
# Test calculator only
pytest tests/test_calculator.py -v

# Test bank account only
pytest tests/test_bank_account.py -v

# Run with coverage for specific module
pytest tests/test_calculator.py --cov=src.calculator
```

### With unittest:
```bash
# Test calculator only
python -m unittest tests.unittest_calculator -v

# Test bank account only
python -m unittest tests.unittest_bank_account -v

# Run specific test class
python -m unittest tests.unittest_calculator.TestCalculator -v

# Run specific test method
python -m unittest tests.unittest_calculator.TestCalculator.test_add_two_positive_numbers -v
```

## Test Patterns Used

### pytest patterns:
- **Setup methods**: `setup_method()` for test initialization
- **Exception testing**: Using `pytest.raises()` for error cases
- **Assertion patterns**: Simple `assert` statements
- **Parametrized tests**: Could be added for multiple input scenarios

### unittest patterns:
- **Setup methods**: `setUp()` for test initialization
- **Exception testing**: Using `assertRaises()` context manager
- **Rich assertions**: `assertEqual()`, `assertAlmostEqual()`, `assertIsInstance()`, etc.
- **Teardown methods**: `tearDown()` for cleanup
- **Test organization**: Multiple test classes for different scenarios

## Framework Comparison

| Feature | pytest | unittest |
|---------|--------|----------|
| Setup | `setup_method()` | `setUp()` |
| Assertions | `assert x == y` | `self.assertEqual(x, y)` |
| Exceptions | `pytest.raises()` | `self.assertRaises()` |
| Float comparison | `assert abs(a-b) < 0.001` | `self.assertAlmostEqual(a, b)` |
| Test discovery | Automatic | `discover()` or `-m unittest` |
| Output verbosity | `-v` flag | `-v` flag or `verbosity=2` |

Try modifying the code and running tests with both frameworks to see TDD in action!