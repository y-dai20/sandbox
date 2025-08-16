# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Test-Driven Development (TDD) educational project demonstrating TDD practices using Jest in Node.js. The project implements simple examples (Calculator) and more complex scenarios (BankAccount with custom exceptions) to show the TDD Red-Green-Refactor cycle in JavaScript.

## Project Architecture

The codebase follows a simple two-layer architecture:

- **`src/`**: Implementation code using CommonJS modules
  - `calculator.js`: Basic arithmetic operations with error handling
  - `bankAccount.js`: Stateful account management with custom `InsufficientFundsError` class
  
- **`tests/`**: Jest test suites with comprehensive coverage
  - `*.test.js`: Jest tests demonstrating TDD patterns and Jest-specific features
  - Organized with nested `describe()` blocks for logical grouping
  - Uses `beforeEach()` for test setup and various Jest matchers

The project showcases Jest-specific testing patterns including custom error testing, floating point assertions, and comprehensive test organization.

## Development Commands

### Testing
```bash
# All tests
npm test

# Watch mode (re-runs tests on file changes)
npm run test:watch

# Coverage report
npm run test:coverage

# Verbose output
npm run test:verbose

# Specific test file
npm test calculator.test.js

# Pattern matching
npm test -- --testNamePattern="deposit"
```

### Setup
```bash
npm install
```

## TDD Workflow

When adding new functionality, follow the established TDD pattern:

1. **Red**: Write failing Jest tests first using `describe()` and `test()` blocks
2. **Green**: Implement minimal code to pass tests
3. **Refactor**: Improve code while maintaining green tests

## Jest Testing Patterns

The project demonstrates key Jest testing patterns:
- **Test organization**: Nested `describe()` blocks for logical grouping
- **Setup**: `beforeEach()` for test initialization
- **Assertions**: Jest matchers like `toBe()`, `toBeCloseTo()`, `toThrow()`, `toBeInstanceOf()`
- **Error testing**: Exception handling with arrow functions and `toThrow()`
- **Floating point**: `toBeCloseTo()` for decimal precision testing
- **Custom errors**: Testing inheritance and error message validation

## Module System

Uses CommonJS (`require`/`module.exports`) for compatibility with Jest's default configuration. Tests import implementations using relative paths.