import unittest
from expense import Expense


class TestCategoryIncome(unittest.TestCase):
    def setUp(self):
        self.expense = Expense(10, 'Food', '12-12-1234')

    def test_str(self):
        self.assertEqual(str(self.expense), '10$ - Food - 12-12-1234 - Expense')

    def test_repr(self):
        self.assertEqual(repr(self.expense), '10$ - Food - 12-12-1234 - Expense')

    def test_eq(self):
        self.assertTrue(self.expense == Expense(10, 'Food', '12-12-1234'))


if __name__ == '__main__':
    unittest.main()
