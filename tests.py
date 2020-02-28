# Author: Ricardo Cousins (cousinsr@oregonstate.edu)
# Course: OSU CS 362, Winter 2020
# Assignment: Assignment 5
# Assignment specification:
# https://oregonstate.instructure.com/courses/1750847/assignments/7761140
# Last modified: 27 February 2020
# Description:
# This program implements unit test test cases for the circleArea(radius), listFirstLast(list), and
# daysBetween(startDate, endDate) functions found in task.py.


import unittest
import math
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    # Test case 1 for circleArea() function
    # Description:
    # Check that circleArea() returns expected output when input radius equals zero.
    def test_circleArea_case1(self):
        # Initialize the test data.
        inputRadius = 0

        # Call the function under test.
        outputArea = task.circleArea(inputRadius)

        # Assert expectations after the function call.
        self.assertEqual(0, outputArea)

    # Test case 2 for circleArea() function
    # Description:
    # Check that circleArea() returns expected output when input radius is less than zero.
    def test_circleArea_case2(self):
        # Initialize the test data.
        inputRadius = -7

        # Call the function under test.
        outputArea = task.circleArea(inputRadius)

        # Assert expectations after the function call.
        self.assertIsNone(None, outputArea)

    # Test case 3 for circleArea() function
    # Description:
    # Check that circleArea() returns expected output when input radius is one.
    def test_circleArea_case3(self):
        # Initialize the test data.
        inputRadius = 1

        # Call the function under test.
        outputArea = task.circleArea(inputRadius)

        # Assert expectations after the function call.
        self.assertEqual(math.pi, outputArea)

    # Test case 4 for circleArea() function
    # Description:
    # Check that circleArea() returns expected output when input radius is 777
    # inclusive.
    def test_circleArea_case4(self):
        # Initialize the test data.
        inputRadius = 777
        expectedArea = math.pi * math.pow(inputRadius, 2)

        # Call the function under test.
        outputArea = task.circleArea(inputRadius)

        # Assert expectations after the function call.
        self.assertEqual(expectedArea, outputArea)


if __name__ == '__main__':
    unittest.main()
