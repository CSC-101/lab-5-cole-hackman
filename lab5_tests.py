import data
import lab5
import math
import unittest
from data import Time, Point
from lab5 import time_add, is_descending, largest_between, largest_between, furthest_from_origin


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        result = time_add(Time(5,30,00), Time(1,30,00))
        expected = Time(7,00,00)
        self.assertEqual(result,expected)

    def test_time_add2(self):
        result = time_add(Time(3,30,50), Time(2,40,20))
        expected = Time(6,11,10)
        self.assertEqual(result,expected)


    # Part 4
    def test_is_descending_1(self):
        result = is_descending([5.0,4.0,3.0,2.0])
        expected = True
        self.assertEqual(result, expected)

    def test_is_descending_2(self):
        result = is_descending([1.0, 2.0, 1.0, 4.0])
        expected = False
        self.assertEqual(result, expected)


    # Part 5
    def test_largest_between_1(self):
        result = largest_between([1,2,3,4,5,6,7,8,9], 2, 8)
        expected = 8
        self.assertEqual(result, expected)

    def test_largest_between_2(self):
        result = largest_between([50,60,10,40,90,70,20,10,80,100], 2, 8)
        expected = 4
        self.assertEqual(result, expected)


    # Part 6
    def test_furthest_from_origin_1(self):
        result = furthest_from_origin([Point(5,10), Point(1,1), Point(20,20)])
        expected = 2
        self.assertEqual(result, expected)

    def test_furthest_from_origin_2(self):
        result = furthest_from_origin([Point(10,10), Point(3,5), Point(9,1), Point(5,8)])
        expected = 0
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
