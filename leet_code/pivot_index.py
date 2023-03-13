"""
This module contains a solution for a LeetCode Problem "724. Find Pivot Index":
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

@author: Olga Aleksandrova
@licence: MIT
"""
from typing import List


def pivot_index(nums: List[int]) -> int:
    """Calculate the pivot index of an array.

    :param nums: array of integers
    :return leftmost pivot index
    """
    # initial sum of array from left to right (0)
    forward_sum = 0
    # initial sum of array from right to left (sum of all the numbers)
    backward_sum = sum(nums)
    # processing sums forward and backward
    for idx, num in enumerate(nums):
        # checking a condition that the sum of elements before pivot index in
        # forward direction is equal to the sum of elements after pivot idx
        backward_sum -= num  # first of all, we need to subtract num of idx from the overall sum
        if forward_sum == backward_sum:
            return idx
        forward_sum += num
    return -1

