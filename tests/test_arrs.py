import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertNotEqual(arrs.get([1, 2, 3], 1, "test"), 3)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 0, "None"), 1)
        self.assertEqual(arrs.get([1, 2, 3, 4, 5, 6, 7], 7, "Not Found"), "Not Found")
        self.assertEqual(arrs.get([1, 2, 3], -1, "Negative number"), "Negative number")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 1), [1])
        self.assertEqual(arrs.my_slice([1, 2, 3], end=2), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5, 6], -5, -2), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5, 6], -6, 6), [1, 2, 3, 4, 5, 6])
        self.assertEqual(arrs.my_slice([]), [])
