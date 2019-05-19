import unittest
from .main import func


class TestTest(unittest.TestCase):
    def test_func(self):
        summ = func(2, 3)
        self.assertEqual(summ, 8)

    def test_func2(self):
        summ = func(2, '3')
        self.assertEqual(summ, 8)

    def test_func2_2(self):
        summ = func(2, 5, 2)
        self.assertEqual(summ, 9)

    def test_func3(self):
        with self.assertRaises(ValueError):
            func(2, 'e')


if __name__ == '__main__':
    unittest.main()