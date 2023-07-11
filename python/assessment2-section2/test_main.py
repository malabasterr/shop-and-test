import unittest
from main import is_isogram, IncorrectInput

# I chose these 4 tests to cover the 4 basic options- valid ture, valid false, invalid and boundary

class MainTestCase(unittest.TestCase):
    def test_is_isogram_true(self): 
        testValue = is_isogram("isogram") # testing that when an isogram is given, it returns True
        self.assertTrue(testValue)

    def test_is_isogram_false(self):
        testValue = is_isogram("hello") # testing that when a word is given but it is not an isogram it returns False
        self.assertFalse(testValue)

    def test_is_isogram_invalid(self):
        testValue = is_isogram("1314") # testing that when an invalid input is given- e.g. not alphabetic characters - it raises an error
        with self.assertRaises(IncorrectInput):
            testValue

    def test_is_isogram_boundary(self):
        testValue = is_isogram("IsoGRam") # testing a boundary case, that when some letters are uppercase, the function still returns True if it is True
        self.assertTrue(testValue)

if __name__ == '__main__':
    unittest.main()