# Author: Ricardo Cousins (cousinsr@oregonstate.edu)
# Course: OSU CS 362, Winter 2020
# Assignment: Assignment 5
# Assignment specification:
# https://oregonstate.instructure.com/courses/1750847/assignments/7761140
# Last modified: 27 February 2020
# Description:
# This program implements the three functions listed below that are required by Assignment 5 specifications.
# circleArea(radius) - accepts radius of a circle and computes and returns the area
# listFirstLast(list) - accepts a list and returns the first and last element in the list
# daysBetween(startDate, endDate) - accepts two dates and returns the number of days between the two dates


import math
import sys


def firstrun():
    return "success"


# This function takes as input the radius of a circle and computes and returns the area of the circle.
# If numerical input less than zero is provided, the function will output a message and return None.
# This function expects that a numerical input is provided.
def circleArea(radius):
    # Ensure that the input radius is 0 or greater.
    if radius < 0:
        print("The radius must be 0 or greater.")
        return None

    # Calculate and return the area of the circle for the provided radius.
    return math.pi * math.pow(radius, 2)
