import unittest

def add(a, b):
    return a + b

class TestCalculator(unittest.TestCase): # Inherit from unittest.TestCase
    def test_add_positive_numbers(self): # Test method must start with 'test_'
        result = add(1, 2)
        self.assertEqual(result, 3) # Use assertion methods

    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)

    def test_add_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    # The following is a snipet of code that will always fail, uncomment it to see what it looks like when code fails the unit test
    
    # def test_purposely_bad(self):
    #     result = add(0,1)
    #     self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()

# To run this unit test enter the following command into the terminal:
# python -m unittest fileName.py

# If the file to test is in a folder run:
# python -m unittest folderName/fileNmae.py