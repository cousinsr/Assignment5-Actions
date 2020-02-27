# Author: Ricardo Cousins (cousinsr@oregonstate.edu)
# Course: OSU CS 362, Winter 2020
# Assignment: Assignment 5
# Assignment specification:
# https://oregonstate.instructure.com/courses/1750847/assignments/7761140
# Last modified: 27 February 2020
# Description:
# This program implements unit test test cases for the circleRadius(radius), listFirstLast(list), and
# daysBetween(startDate, endDate) functions found in task.py.


import unittest
import task


class TestCase(unittest.TestCase):

	def test1(self):
		expected = "success"
		self.assertEqual(expected, task.firstrun())
	
	def test2(self):
		expected = "failure"
		self.assertNotEqual(expected, task.firstrun())


if __name__ == '__main__':
	unittest.main()
