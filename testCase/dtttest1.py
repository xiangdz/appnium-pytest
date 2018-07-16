import unittest
from ddt import ddt, data, unpack


# @ddt
# class MyTestCase1(unittest.TestCase):
#     @data(1, 2)
#     @unpack
#     def test_normal(self, value):
#         print(value)
#         self.assertEqual(value, 2)

import unittest
from ddt import ddt, data
# from ddt_demo.mycode import larger_than_two


@ddt
class FooTestCase(unittest.TestCase):
    def larger_than_two(self,value):
        return int(value)


    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        self.assertTrue(FooTestCase.larger_than_two(value))

    @data(1, -3, 2, 0)
    def test_not_larger_than_two(self, value):
        self.assertTrue(FooTestCase.larger_than_two(value))


    @data(u'ascii', u'non-ascii-\N{SNOWMAN}')
    def test_unicode(self, value):
        self.assertIn(value, (u'ascii', u'non-ascii-\N{SNOWMAN}'))


if __name__ == '__main__':
    unittest.main(verbosity=2)

#
# if __name__ == '__main__':
#     unittest.main()
