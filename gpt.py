# https://chat.openai.com/c/0b230461-1118-40a2-9aea-3c8b59130d18
import unittest

# Simple function that adds two numbers
def add(a, b):
    return a + b

# Test case for the add function
class TestAddFunction(unittest.TestCase):
    # Test method for positive numbers
    def test_add_positive_numbers(self):
        # Asserts that add(2, 3) returns 5
        self.assertEqual(add(2, 3), 5)

    # Test method for negative numbers
    def test_add_negative_numbers(self):
        # Asserts that add(-1, -1) returns -2
        self.assertEqual(add(-1, -1), -2)

    # Test method for adding zeros
    def test_add_zero(self):
        # Asserts that add(0, 0) returns 0
        self.assertEqual(add(0, 0), 0)


if __name__ == '__main__':
    unittest.main()