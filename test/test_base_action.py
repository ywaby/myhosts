import unittest
from myhosts import base_action


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_d(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_c(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
