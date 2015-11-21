import unittest
from nth_prime import *

class TestPrimes(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))

    def test_prime(self):
        self.assertEqual(prime(5), 11)
        #self.assertEqual(prime(1), 2)
        self.assertEqual(prime(10), 29)
        self.assertEqual(prime(105), 571)


if __name__ == '__main__':
    unittest.main()
