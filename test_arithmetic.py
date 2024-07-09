import unittest
from grin.arithmetic import Arithmetic


class TestArithmetic(unittest.TestCase):
    """Tests Arithmetic class"""
    def test_add_int(self):
        """tests adding integers"""
        arithmetic = Arithmetic()
        result = arithmetic.add(3, 4)
        self.assertEqual(result, 7)

    def test_add_string(self):
        """tests adding strings"""
        arithmetic = Arithmetic()
        result = arithmetic.add("hello", "world")
        self.assertEqual(result, "hello world")

    def test_sub_int(self):
        """tests subtraction for int"""
        arithmetic = Arithmetic()
        result = arithmetic.sub(5,3)
        self.assertEqual(result, 2)

    def test_mult_int(self):
        """tests multiplying ints"""
        arithmetic = Arithmetic()
        result = arithmetic.mult(5, 2)
        self.assertEqual(result, 10)

    def test_mult_str_int(self):
        """tests str * int"""
        arithmetic = Arithmetic()
        result = arithmetic.mult("*", 3)
        self.assertEqual(result, "***")

    def test_div_int(self):
        """tests int/int"""
        arithmetic = Arithmetic()
        result = arithmetic.div(10, 2)
        self.assertEqual(result, 5)

    def test_div_float(self):
        """tests float/float"""
        arithmetic = Arithmetic()
        result = arithmetic.div(7,2)
        self.assertEqual(result, 3)

    def test_div_zero(self):
        """checks for assert a/0 triggers exception"""
        arithmetic = Arithmetic()
        with self.assertRaises(ZeroDivisionError):
            arithmetic.div(8,0)

    def test_error_add(self):
        """tests for exception in addition"""
        arithmetic = Arithmetic()
        result = arithmetic.add(2, "a")
        self.assertIsNone(result)

    def test_error_sub(self):
        """tests for exception in subtraction"""
        arithmetic = Arithmetic()
        result = arithmetic.add(2, "a")
        self.assertIsNone(result)

    def test_error_mult(self):
        """tests for exception in mult"""
        arithmetic = Arithmetic()
        result = arithmetic.add(2, "a")
        self.assertIsNone(result)

    def test_error_div(self):
        """tests for exception for dividing"""
        arithmetic = Arithmetic()
        result = arithmetic.add(2, "a")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
