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
import datetime


def firstrun():
    return "success"


# This function takes as input the radius of a circle and computes and returns the area of the circle.
# If numerical input less than zero is provided, the function will output a message and return None.
# This function expects that a numerical input is provided.
def circleArea(radius):
    # Ensure that the input radius is 0 or greater.
    if radius < 0:
        print("The input radius must be 0 or greater.")
        return None

    # Calculate and return the area of the circle for the provided radius.
    return math.pi * math.pow(radius, 2)


# This function takes as input a list and returns in a tuple the first and last element in the list.
# This function expects that a list is provided an input.
def listFirstLast(list):
    # Ensure that the input list has a length of 1 or greater.
    if len(list) < 1:
        print("The input list must contain 1 or more elements.")
        return None

    # Return the first and last elements of the list in a tuple.
    return list[0], list[len(list) - 1]


# This function takes as input two dates and returns the number of days between the two dates.
# This function expects that each input date is of type datetime.date. The scenario of mixed inputs of type
# datetime.date and datetime.datetime is not supported or gracefully blocked by this function.
# https://docs.python.org/3.6/library/datetime.html#datetime.date
def daysBetween(startDate, endDate):
    # Ensure that both inputs are of datetime.date format.
    if isinstance(startDate, datetime.date) is False or isinstance(endDate, datetime.date) is False:
        print("Both inputs must have datetime.date format.")
        return None

    # Calculate and return the number of days between the two input dates.
    days = endDate - startDate
    return days.days
