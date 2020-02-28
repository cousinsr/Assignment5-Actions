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
import datetime
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
        self.assertIsNone(outputArea)

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

    # Test case 1 for listFirstLast() function
    # Description:
    # Check that listFirstLast() returns expected output when the input list is empty.
    def test_listFirstLast_case1(self):
        # Initialize the test data.
        inputList = []

        # Call the function under test.
        outputDataContainer = task.listFirstLast(inputList)

        # Assert expectations after the function call.
        self.assertIsNone(outputDataContainer)

    # Test case 2 for listFirstLast() function
    # Description:
    # Check that listFirstLast() returns expected output when the input list contains one element.
    def test_listFirstLast_case2(self):
        # Initialize the test data.
        inputList = [7]
        expectedOutput = (7, 7)

        # Call the function under test.
        outputDataContainer = task.listFirstLast(inputList)

        # Assert expectations after the function call.
        self.assertEqual(expectedOutput, outputDataContainer)

    # Test case 3 for listFirstLast() function
    # Description:
    # Check that listFirstLast() returns expected output when the input list contains two unique elements.
    def test_listFirstLast_case3(self):
        # Initialize the test data.
        inputList = [7, 12]
        expectedOutput = (7, 12)

        # Call the function under test.
        outputDataContainer = task.listFirstLast(inputList)

        # Assert expectations after the function call.
        self.assertEqual(expectedOutput, outputDataContainer)

    # Test case 4 for listFirstLast() function
    # Description:
    # Check that listFirstLast() returns expected output when the input list contains eleven unique elements.
    def test_listFirstLast_case4(self):
        # Initialize the test data.
        inputList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expectedOutput = (0, 10)

        # Call the function under test.
        outputDataContainer = task.listFirstLast(inputList)

        # Assert expectations after the function call.
        self.assertEqual(expectedOutput, outputDataContainer)

    # Test case 5 for listFirstLast() function
    # Description:
    # Check that listFirstLast() returns expected output when the input list contains 3 unique elements that
    # are a mixture of integers and strings.
    def test_listFirstLast_case5(self):
        # Initialize the test data.
        inputList = [0, 1, "third element"]
        expectedOutput = (0, "third element")

        # Call the function under test.
        outputDataContainer = task.listFirstLast(inputList)

        # Assert expectations after the function call.
        self.assertEqual(expectedOutput, outputDataContainer)

    # Test case 1 for daysBetween() function
    # Description:
    # Check that daysBetween() returns expected output when an input is not of type datetime.date.
    def test_daysBetween_case1(self):
        # Initialize the test data.
        date1 = datetime.date(2020, 2, 27)
        date2 = "more junk"

        # Call the function under test.
        daysOutput = task.daysBetween(date1, date2)

        # Assert expectations after the function call.
        self.assertIsNone(daysOutput)

    # Test case 2 for daysBetween() function
    # Description:
    # Check that daysBetween() returns expected output when the input dates are the same date.
    def test_daysBetween_case2(self):
        # Initialize the test data.
        date1 = datetime.date(2020, 2, 28)
        date2 = datetime.date(2020, 2, 28)

        # Call the function under test.
        daysOutput = task.daysBetween(date1, date2)

        # Assert expectations after the function call.
        self.assertEqual(0, daysOutput)

    # Test case 3 for daysBetween() function
    # Description:
    # Check that daysBetween() returns expected output when the input dates are the consecutive.
    def test_daysBetween_case3(self):
        # Initialize the test data.
        date1 = datetime.date(2020, 2, 27)
        date2 = datetime.date(2020, 2, 28)

        # Call the function under test.
        daysOutput = task.daysBetween(date1, date2)

        # Assert expectations after the function call.
        self.assertEqual(1, daysOutput)

    # Test case 4 for daysBetween() function
    # Description:
    # Check that daysBetween() returns expected output when the first input date is later than the second
    # input date.
    def test_daysBetween_case4(self):
        # Initialize the test data.
        date1 = datetime.date(2020, 2, 27)
        date2 = datetime.date(2020, 2, 17)

        # Call the function under test.
        daysOutput = task.daysBetween(date1, date2)

        # Assert expectations after the function call.
        self.assertEqual(-10, daysOutput)

    # Test case 5 for daysBetween() function
    # Description:
    # Check that daysBetween() returns expected output when the second input date is a special leap year day
    # in February 2020.
    def test_daysBetween_case5(self):
        # Initialize the test data.
        date1 = datetime.date(2020, 2, 27)
        date2 = datetime.date(2020, 2, 29)

        # Call the function under test.
        daysOutput = task.daysBetween(date1, date2)

        # Assert expectations after the function call.
        self.assertEqual(2, daysOutput)


if __name__ == '__main__':
    unittest.main()
