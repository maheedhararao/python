import unittest


class Test3(unittest.TestCase):
    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual('a' * 4, 'aaaa')

    # Returns True if the string is in upper case.
    def test_upper(self):
        print('Running test from Test3')
        self.assertEqual('foo'.upper(), 'FOO')
