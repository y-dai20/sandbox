const Calculator = require('../src/calculator');

describe('Calculator', () => {
  let calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  describe('add', () => {
    test('should add two positive numbers', () => {
      const result = calculator.add(2, 3);
      expect(result).toBe(5);
    });

    test('should add positive and negative number', () => {
      const result = calculator.add(5, -3);
      expect(result).toBe(2);
    });

    test('should add two negative numbers', () => {
      const result = calculator.add(-2, -3);
      expect(result).toBe(-5);
    });

    test('should handle floating point addition', () => {
      const result = calculator.add(2.5, 3.7);
      expect(result).toBeCloseTo(6.2);
    });
  });

  describe('subtract', () => {
    test('should subtract two positive numbers', () => {
      const result = calculator.subtract(5, 3);
      expect(result).toBe(2);
    });

    test('should subtract negative from positive', () => {
      const result = calculator.subtract(5, -3);
      expect(result).toBe(8);
    });

    test('should handle floating point subtraction', () => {
      const result = calculator.subtract(5.5, 2.2);
      expect(result).toBeCloseTo(3.3);
    });
  });

  describe('multiply', () => {
    test('should multiply two positive numbers', () => {
      const result = calculator.multiply(3, 4);
      expect(result).toBe(12);
    });

    test('should multiply by zero', () => {
      const result = calculator.multiply(5, 0);
      expect(result).toBe(0);
    });

    test('should multiply negative numbers', () => {
      const result = calculator.multiply(-3, -4);
      expect(result).toBe(12);
    });

    test('should multiply positive and negative', () => {
      const result = calculator.multiply(3, -4);
      expect(result).toBe(-12);
    });
  });

  describe('divide', () => {
    test('should divide two positive numbers', () => {
      const result = calculator.divide(10, 2);
      expect(result).toBe(5);
    });

    test('should divide and return decimal', () => {
      const result = calculator.divide(7, 2);
      expect(result).toBe(3.5);
    });

    test('should divide zero by number', () => {
      const result = calculator.divide(0, 5);
      expect(result).toBe(0);
    });

    test('should throw error when dividing by zero', () => {
      expect(() => {
        calculator.divide(10, 0);
      }).toThrow('Cannot divide by zero');
    });

    test('should handle floating point division', () => {
      const result = calculator.divide(5.5, 2.2);
      expect(result).toBeCloseTo(2.5);
    });
  });

  test('should be an instance of Calculator', () => {
    expect(calculator).toBeInstanceOf(Calculator);
  });
});