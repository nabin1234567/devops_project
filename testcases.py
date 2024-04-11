import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add_success(self):
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract_success(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply_success(self):
        result = multiply(2, 5)
        self.assertEqual(result, 6)

    def test_divide_by_zero_fail(self):
        result = divide(8, 0)
        self.assertEqual(result, "Cannot divide by zero!")

    def test_divide_success(self):
        result = divide(10, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
