import pytest
from leet_code.is_isomorphic import is_isomorphic


@pytest.mark.parametrize(
    ["first", "second", "expected"],
    [
        ("badc", "baba", False),
        ("paper", "title", True),
        ("foo", "bar", False),
        ("egg", "add", True),
    ]
)
def test_simple(first: str, second: str, expected: bool):
    assert is_isomorphic(first, second) == expected


def test_not_fail_on_empty():
    is_isomorphic("", "test")

