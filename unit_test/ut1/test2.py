import unittest


class Test2(unittest.TestCase):
    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        print('Running test from Test2')
        self.assertEqual('a' * 4, 'aaaa')

    # Returns True if the string is in upper case.
    def test_upper(self):
        print('Running test from Test2')
        self.assertEqual('foo'.upper(), 'FOO')

    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):
        print('Running test from Test2')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == "__main__":
    unittest.main()
