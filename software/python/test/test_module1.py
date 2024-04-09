# test_module1.py

import unittest
from module1 import greet, add

class TestModule1(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
