from typing import List
from leet_code import utils, print_hello


def pivot_index(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    err_val = -1  # setting error value
    forward_sum = 0  # initial sum of array from left to right (0)
    backward_sum = sum(nums)  # initial sum of array from right to left
    # (sum of all the numbers)
    # processing sums forward and backward
    for idx, num in enumerate(nums):
        # checking a condition that the sum of elements before pivot index in
        # forward direction is equal to the sum of elements after pivot idx
        backward_sum -= num  # first of all, we need to subtract num of idx from the overall sum
        if forward_sum == backward_sum:
            return idx
        forward_sum += num
    return err_val


test_nums_1 = [1, 7, 3, 6, 5, 6]
test_nums_2 = [2, 1, -1]
test_nums_3 = [-1, 1, 2]
test_nums_4 = [1, 2, 3]

print(pivot_index(test_nums_1))
print(pivot_index(test_nums_2))
print(pivot_index(test_nums_3))
print(pivot_index(test_nums_4))


def square(sequence : List[int]):
    for x in sequence:
        ...
        print("s", x)
        yield x*x
    if len(sequence) > 4:
        return
    for x in sequence:
        print("s2", x)
        yield x * x


if __name__ == '__main__':
    for z in square([1,2,3,4,5]):
        print("z", z)
    utils.print_hello()
    print_hello()
