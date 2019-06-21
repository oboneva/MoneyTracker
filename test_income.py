import unittest
from income import Income


class TestCategoryIncome(unittest.TestCase):
    def setUp(self):
        self.income = Income(10, 'Food', '12-12-1234')

    def test_str(self):
        self.assertEqual(str(self.income), '10$ - Food - 12-12-1234 - Income')

    def test_repr(self):
        self.assertEqual(repr(self.income), '10$ - Food - 12-12-1234 - Income')

    def test_eq(self):
        self.assertTrue(self.income == Income(10, 'Food', '12-12-1234'))


if __name__ == '__main__':
    unittest.main()
