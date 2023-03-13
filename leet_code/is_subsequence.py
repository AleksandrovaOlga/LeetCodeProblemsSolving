"""
This module contains a solution for a LeetCode Problem "392. Is Subsequence":
Given two strings first_string and second_string, return true if first_string is a subsequence of second_string,
or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not). Both strings consist only of lowercase English letters.

@author: Olga Aleksandrova
@licence: MIT
"""


def is_subsequence_first_variant(first_str: str, second_str: str) -> bool:
    """Check if first string is a substring of second string.

    :param first_str: subsequence as a string
    :param second_str: target string
    :return: true  if first_str is a substring of second_str, false - otherwise
    """
    if not set(first_str).issubset(second_str) or len(first_str) > len(second_str):
        return False
    idx_in_second_str = 0
    find_char_count = 0
    for char_in_first_str in first_str:
        for char_in_second_str in second_str[idx_in_second_str:]:
            idx_in_second_str += 1
            if char_in_first_str == char_in_second_str:
                find_char_count += 1
                break
    return find_char_count == len(first_str)


def is_subsequence_second_variant(first_str: str, second_str: str) -> bool:
    """Check if first string is a substring of second string.

        :param first_str: subsequence as a string
        :param second_str: target string
        :return: true  if first_str is a substring of second_str, false - otherwise
    """
    if len(first_str) > len(second_str):
        return False
    if not first_str:
        return True
    subsequence = 0
    for char_in_second_str in second_str:
        if (
            subsequence <= len(first_str) - 1
            and first_str[subsequence] == char_in_second_str
        ):
            subsequence += 1
    return subsequence == len(first_str)
