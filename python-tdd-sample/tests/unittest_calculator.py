import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_two_positive_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_positive_and_negative_number(self):
        result = self.calc.add(5, -3)
        self.assertEqual(result, 2)

    def test_add_two_negative_numbers(self):
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)

    def test_subtract_two_positive_numbers(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtract_negative_from_positive(self):
        result = self.calc.subtract(5, -3)
        self.assertEqual(result, 8)

    def test_multiply_two_positive_numbers(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_multiply_by_zero(self):
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)

    def test_multiply_negative_numbers(self):
        result = self.calc.multiply(-3, -4)
        self.assertEqual(result, 12)

    def test_divide_two_positive_numbers(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

    def test_divide_zero_by_number(self):
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)

    def test_calculator_instance_creation(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_add_with_floats(self):
        result = self.calc.add(2.5, 3.7)
        self.assertAlmostEqual(result, 6.2, places=1)

    def test_divide_returns_float(self):
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)
        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()
