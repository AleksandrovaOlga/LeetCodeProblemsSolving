"""
This module contains a solution for a LeetCode Problem "205. Isomorphic Strings":
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

@author: Olga Aleksandrova
@licence: MIT
"""


def is_isomorphic(first_str: str, second_str: str) -> bool:
    """Calculate if two strings are isomorphic.

    Two strings are isomorphic if the characters in first string can be replaced to get second string.

    :param first_str: first string to compare
    :param second_str: second string to compare
    :return: true if isomorphic else otherwise
    """
    # dictionary, which maps characters of first_str as keys and characters of second_str as values
    dict_first_str_to_second_str = {}
    # final word constructed from map
    constructed_word = ""
    for character_from_first_str, character_from_second_str in zip(first_str, second_str):
        char_from_first_str_value = dict_first_str_to_second_str.get(character_from_first_str)
        if char_from_first_str_value is None and character_from_second_str not in dict_first_str_to_second_str.values():
            dict_first_str_to_second_str[character_from_first_str] = character_from_second_str
        elif char_from_first_str_value is None or char_from_first_str_value != character_from_second_str:
            return False
        constructed_word += dict_first_str_to_second_str[character_from_first_str]
    return second_str == constructed_word
