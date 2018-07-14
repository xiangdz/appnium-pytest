import unittest
from ddt import ddt, data, unpack


@ddt
class MyTestCase1(unittest.TestCase):
    @data(1, 2, 3)
    def test_normal(self, value):
        print(value)
        self.assertEqual(value, 2)


if __name__ == '__main__':
    unittest.main()
