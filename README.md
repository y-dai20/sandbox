# TDD Learning Sandbox

This repository contains multiple Test-Driven Development (TDD) sample projects demonstrating TDD principles across different programming languages and testing frameworks.

## What is Test-Driven Development?

Test-Driven Development (TDD) is a software development methodology that follows a simple cycle:

1. **🔴 Red**: Write a failing test first
2. **🟢 Green**: Write the minimum code to make the test pass  
3. **🔵 Refactor**: Improve the code while keeping tests green

## Projects Overview

### 📁 `python-tdd-sample/`
**Python TDD with pytest and unittest**

A comprehensive Python project demonstrating TDD using both pytest and unittest frameworks side-by-side for comparison.

**Features:**
- Calculator class (simple TDD example)
- BankAccount class (complex TDD with custom exceptions)
- Side-by-side pytest and unittest implementations
- Comprehensive test coverage patterns

**Key Files:**
- `tests/test_*.py` - pytest versions
- `tests/unittest_*.py` - unittest versions  
- `src/calculator.py` & `src/bank_account.py` - implementations

**Setup & Run:**
```bash
cd python-tdd-sample
pip install -r requirements.txt

# pytest
pytest

# unittest  
python -m unittest discover tests -p "unittest_*.py" -v
```

### 📁 `nodejs-tdd-jest/`
**Node.js TDD with Jest**

A Node.js project showcasing TDD practices using the Jest testing framework with modern JavaScript patterns.

**Features:**
- Calculator class (basic arithmetic with error handling)
- BankAccount class (stateful operations with custom errors)
- Jest-specific testing patterns and matchers
- Coverage reporting and watch mode

**Key Files:**
- `tests/*.test.js` - Jest test files
- `src/*.js` - CommonJS implementations
- `package.json` - Jest configuration

**Setup & Run:**
```bash
cd nodejs-tdd-jest
npm install

# Run tests
npm test

# Watch mode
npm run test:watch

# Coverage
npm run test:coverage
```

## Learning Objectives

Each project demonstrates:

### Core TDD Principles
- Writing tests before implementation
- Minimal code to pass tests
- Continuous refactoring
- Red-Green-Refactor cycle

### Testing Patterns
- Test organization and naming
- Setup and teardown methods
- Exception/error testing
- Edge case coverage
- Floating point precision handling

### Framework-Specific Features

**Python (pytest vs unittest):**
- Simple `assert` vs rich assertion methods
- `pytest.raises()` vs `assertRaises()`
- `setup_method()` vs `setUp()`
- Test discovery differences

**JavaScript (Jest):**
- `describe()` and `test()` organization
- Jest matchers (`toBe`, `toBeCloseTo`, `toThrow`)
- `beforeEach()` setup patterns
- Coverage reporting

## Getting Started

1. **Choose a project** based on your preferred language
2. **Follow the setup instructions** in each project's README
3. **Examine the tests first** to understand expected behavior
4. **Run the tests** to see them pass
5. **Try breaking the implementation** to see tests fail
6. **Practice TDD** by adding new features:
   - Write failing tests first
   - Implement minimal code
   - Refactor while keeping tests green

## Common Example Classes

Both projects implement similar classes for comparison:

### Calculator
- `add(a, b)` - Addition with number and float support
- `subtract(a, b)` - Subtraction 
- `multiply(a, b)` - Multiplication including edge cases
- `divide(a, b)` - Division with zero-division error handling

### BankAccount  
- `constructor/init(initial_balance)` - Account initialization
- `deposit(amount)` - Add funds with validation
- `withdraw(amount)` - Remove funds with insufficient funds checking
- `getBalance()` - Current balance retrieval
- Custom exception handling for invalid operations

## Best Practices Demonstrated

- **Descriptive test names** that explain behavior
- **Comprehensive edge case testing** (zero values, negative numbers, floating point)
- **Error condition testing** with custom exceptions
- **State verification** in stateful objects
- **Test isolation** with proper setup/teardown
- **Clear assertion messages** for debugging

## Next Steps

After exploring these examples:

1. **Practice** by adding new methods to existing classes
2. **Experiment** with different testing patterns
3. **Apply TDD** to your own projects
4. **Compare** how different frameworks handle similar testing scenarios

Happy coding and testing! 🚀