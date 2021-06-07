import unittest
import example


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(example.subtract(1, 1), 0)

    def test_division(self):
        self.assertEqual(example.division(5, 1), 5)

    def test_multiply(self):
        self.assertEqual(example.multiply(5, 1), 5)


if __name__ == '__main__':
    unittest.main()
