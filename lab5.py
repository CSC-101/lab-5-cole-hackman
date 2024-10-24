import data
import math
from data import Time
from data import Point

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# Purpose: Adds two Time objects together, taking into account any overflow of minutes and seconds, and returns the resulting Time object.
# Input: Two Time objects (time1, time2) representing hours, minutes, and seconds.
# Output: A Time object representing the sum of the two input times, with proper adjustment for any overflow of minutes or seconds.
def time_add(time1: Time, time2: Time) -> Time:
    sum_hours = time1.hour + time2.hour
    sum_minutes = time1.minute + time2.minute
    sum_seconds = time1.second + time2.second
    if (sum_minutes) >= 60:
        sum_hours += (sum_minutes // 60)
        sum_minutes = sum_minutes % 60
    if (sum_seconds) >= 60:
        sum_minutes += (sum_seconds // 60)
        sum_seconds = sum_seconds % 60
    return Time(sum_hours, sum_minutes, sum_seconds)


# Part 4
# Purpose: Checks if a list of floating-point numbers is in strictly descending order.
# Input: A list of floating-point numbers (inputList).
# Output: A boolean value indicating whether the list is in descending order (True if descending, False otherwise).
def is_descending(inputList: list[float]) -> bool:
    counter = 0
    for num in range(1,len(inputList)):
        if inputList[num] > inputList[num-1]:
            return False
    return True


# Part 5
# Purpose: Finds the index of the largest integer in a sublist defined by the range of indices [lower, upper]. Returns None if the bounds are invalid.
# Input: A list of integers (inputList), and two integer indices (lower, upper) defining the range of interest.
# Output: The index of the largest integer in the sublist or None if the input bounds are invalid.
# I decided that if lower or upper is out of bounds, the function will return None
def largest_between(inputList: list[int], lower: int, upper: int):
    if (lower > upper) or (lower < 0) or (upper >= len(inputList)):
        return None
    idx = lower
    for num in range(lower, upper+1):
        if inputList[num] > inputList[idx]:
            idx = num

    return idx


# Part 6
# Purpose: Finds the point that is furthest from the origin (0, 0) based on the Euclidean distance.
# Input: A list of Point objects (inputList), where each Point has x and y coordinates.
# Output: The index of the point in the list that is furthest from the origin, or None if the list is empty.
def furthest_from_origin(inputList: list[Point]) -> Point:
    if len(inputList) == 0:
        return None

    origin = Point(0,0)
    furthest_idx = 0
    furthest = math.sqrt(inputList[0].x**2 + inputList[0].y**2)
    for i in range(1, len(inputList)):
        point = inputList[i]
        distance = math.sqrt(point.x**2 + point.y**2)
        if distance > furthest:
            furthest = distance
            furthest_idx = i

    return furthest_idx