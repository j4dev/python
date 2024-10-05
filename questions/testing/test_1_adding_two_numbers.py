import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _1_adding_two_numbers import addNumbers

class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        print("\nStarting a new test...")

    def test_add_floats(self):
        inputs_outputs = [
            ((2.3, 1.9), 4),
            ((2.34, 5.7), 8)
        ]

        for inputs, expected in inputs_outputs:
            a, b = inputs
            print(f"Input: a = {a}, b = {b}")
            result = addNumbers(a, b)
            print(f"Output: {result}")
            self.assertEqual(result, expected)
            print(f"Expected: {expected}, Test {'Passed' if result == expected else 'Failed'}")

if __name__ == '__main__':
    unittest.main()