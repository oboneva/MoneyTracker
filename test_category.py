import unittest
from category import Category

class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category(10, 'Food', '22-03-2018')

    def test_str(self):
        self.assertEqual(str(self.category), '10$ - Food - 22-03-2018')

    def test_repr(self):
        self.assertEqual(repr(self.category), '10$ - Food - 22-03-2018')

    def test_eq(self):
        self.assertTrue(self.category == Category(10, 'Food', '22-03-2018'))

    def test_raises_value_error(self):
        with self.assertRaises(ValueError):
            Category(-10, 'Food', '20-12-2019')

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            Category('sdsd', 'Food', '20-12-2019')


if __name__ == '__main__':
    unittest.main()
