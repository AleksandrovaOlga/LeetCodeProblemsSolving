import pytest
from leet_code.is_subsequence import is_subsequence_second_variant, is_subsequence_first_variant


@pytest.mark.parametrize(
    ["first", "second", "expected"],
    [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("abbccc", "andaaabbbxxccc", True),
        ("acb", "ahbgdc", False),
        ("aaaaaa", "bbaaaa", False),
    ]
)
def test_substrings(first: str, second: str, expected: bool):
    assert is_subsequence_first_variant(first, second) == expected
    assert is_subsequence_second_variant(first, second) == expected
