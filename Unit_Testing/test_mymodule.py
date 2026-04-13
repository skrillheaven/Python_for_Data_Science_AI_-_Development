import unittest

from mymodule import square , double

class TestMyCodeSquare(unittest.TestCase):

    def test_square(self):

        self.assertEqual(square(2) , 4) # When 2 is given as input the output must be 4.
        self.assertEqual(square(3.0) , 9) # When 3.0 is given as input the output must be 9.0
        self.assertNotEqual(square(-3) , -9) # When -3 is given as input the output must not be -9.

class TestMyCodeDouble(unittest.TestCase):

    def test_double(self):
        self.assertEqual(double(2) , 4) # When 2 is given as input the output must be 4.
        self.assertEqual(double(-3.1) , -6.2) # When -3.1 is given as input the output must be -6.2.
        self.assertEqual(double(0) , 0) # When 0 is given as input the output must be 0.

unittest.main()

