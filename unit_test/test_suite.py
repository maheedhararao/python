from test1 import Test1
from test2 import Test2
from test3 import Test3

import unittest


def suite():
    suite1 = unittest.TestSuite()
    suite1.addTest(Test3('test_upper'))
    suite1.addTest(Test2('test_isupper'))
    suite1.addTest(Test1('test_strings_a'))
    return suite1


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())