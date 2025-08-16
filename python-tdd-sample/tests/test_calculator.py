import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add_two_positive_numbers(self):
        result = self.calc.add(2, 3)
        assert result == 5

    def test_add_positive_and_negative_number(self):
        result = self.calc.add(5, -3)
        assert result == 2

    def test_add_two_negative_numbers(self):
        result = self.calc.add(-2, -3)
        assert result == -5

    def test_subtract_two_positive_numbers(self):
        result = self.calc.subtract(5, 3)
        assert result == 2

    def test_subtract_negative_from_positive(self):
        result = self.calc.subtract(5, -3)
        assert result == 8

    def test_multiply_two_positive_numbers(self):
        result = self.calc.multiply(3, 4)
        assert result == 12

    def test_multiply_by_zero(self):
        result = self.calc.multiply(5, 0)
        assert result == 0

    def test_multiply_negative_numbers(self):
        result = self.calc.multiply(-3, -4)
        assert result == 12

    def test_divide_two_positive_numbers(self):
        result = self.calc.divide(10, 2)
        assert result == 5

    def test_divide_by_zero_raises_exception(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

    def test_divide_zero_by_number(self):
        result = self.calc.divide(0, 5)
        assert result == 0
