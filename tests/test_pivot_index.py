import pytest
from leet_code.pivot_index import pivot_index

from typing import List


@pytest.mark.parametrize(
    ["int_list", "expected_pivot_idx"],
    [
        ([1, 7, 3, 6, 5, 6], 3),
        ([2, 1, -1], 0),
        ([-1, 1, 2], 2),
        ([1, 2, 3], -1),
    ]
)
def test_simple(int_list: List[int], expected_pivot_idx: int):
    assert pivot_index(int_list) == expected_pivot_idx
