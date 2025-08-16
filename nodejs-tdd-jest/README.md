# Node.js TDD Sample Project with Jest

This project demonstrates Test-Driven Development (TDD) practices in Node.js using the Jest testing framework.

## What is TDD?

Test-Driven Development (TDD) is a software development methodology where you:

1. **Red**: Write a failing test first
2. **Green**: Write the minimum code to make the test pass
3. **Refactor**: Improve the code while keeping tests green

## Project Structure

```
nodejs-tdd-jest/
├── src/
│   ├── calculator.js      # Simple calculator implementation
│   └── bankAccount.js     # Bank account with custom exceptions
├── tests/
│   ├── calculator.test.js
│   └── bankAccount.test.js
├── package.json
├── .gitignore
└── README.md
```

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run all tests:
   ```bash
   npm test
   ```

3. Run tests in watch mode:
   ```bash
   npm run test:watch
   ```

4. Run tests with coverage:
   ```bash
   npm run test:coverage
   ```

5. Run tests with verbose output:
   ```bash
   npm run test:verbose
   ```

## Examples

### Calculator (Simple TDD Example)

The `Calculator` class demonstrates basic TDD with simple mathematical operations:
- Addition, subtraction, multiplication, division
- Error handling for division by zero
- Floating point arithmetic with `toBeCloseTo()` matcher

### BankAccount (Complex TDD Example)

The `BankAccount` class shows more complex TDD scenarios:
- State management (balance tracking)
- Custom exceptions (`InsufficientFundsError`)
- Input validation
- Edge cases (zero amounts, exact balance withdrawals)
- Floating point precision handling

## TDD Process Demonstrated

1. **Write tests first** (`*.test.js` files)
   - Define expected behavior with `describe` and `test` blocks
   - Include edge cases and error conditions
   - Use descriptive test names

2. **Run tests** (they should fail initially)
   ```bash
   npm test
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

## Jest Features Demonstrated

### Test Organization
- **Test suites**: `describe()` blocks for grouping related tests
- **Setup/teardown**: `beforeEach()` for test initialization
- **Nested describes**: Logical grouping of functionality

### Assertions and Matchers
- **Equality**: `toBe()` for exact equality, `toEqual()` for object equality
- **Floating point**: `toBeCloseTo()` for decimal precision
- **Type checking**: `toBeInstanceOf()` for type validation
- **Error testing**: `toThrow()` for exception handling

### Advanced Patterns
- **Custom error classes**: Testing inheritance with `InsufficientFundsError`
- **Edge case testing**: Boundary conditions and floating point precision
- **State verification**: Ensuring object state changes correctly

## Running Individual Tests

```bash
# Run specific test file
npm test calculator.test.js
npm test bankAccount.test.js

# Run specific test suite
npm test -- --testNamePattern="Calculator"
npm test -- --testNamePattern="deposit"

# Run with pattern matching
npm test -- --testPathPattern="calculator"

# Watch specific file
npm test -- --watch calculator.test.js
```

## Coverage Reports

Jest provides built-in coverage reporting:

```bash
# Generate coverage report
npm run test:coverage

# View HTML coverage report
open coverage/lcov-report/index.html
```

## Jest Configuration

The project uses Jest configuration in `package.json`:

```json
{
  "jest": {
    "testEnvironment": "node",
    "collectCoverageFrom": ["src/**/*.js"],
    "coverageDirectory": "coverage"
  }
}
```

## Test Patterns Used

### Setup and Teardown
```javascript
beforeEach(() => {
  calculator = new Calculator();
});
```

### Grouped Testing
```javascript
describe('Calculator', () => {
  describe('add', () => {
    test('should add two positive numbers', () => {
      // test implementation
    });
  });
});
```

### Exception Testing
```javascript
test('should throw error when dividing by zero', () => {
  expect(() => {
    calculator.divide(10, 0);
  }).toThrow('Cannot divide by zero');
});
```

### Floating Point Testing
```javascript
test('should handle floating point addition', () => {
  const result = calculator.add(2.5, 3.7);
  expect(result).toBeCloseTo(6.2);
});
```

Try modifying the code and running tests to see TDD in action with Jest!