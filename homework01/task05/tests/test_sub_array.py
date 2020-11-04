from typing import List

import pytest
from sub_array.sub_array import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["data", "size", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([0], 3, 0),
        ([5], 5, 5),
        ([30, 1], 2, 31),
        ([30, 1], 5, 31),
        ([30, 1, -1], 5, 31),
        ([20, 20, -20], 3, 40),
    ],
)
def test_find_max_subarray(data: List[int], size: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(data, size)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["data", "size"],
    [
        ([10], 0),
        ([5], -2),
    ],
)
def test_input_exception(data: List[int], size: int):
    with pytest.raises(ValueError):
        assert find_maximal_subarray_sum(data, size)
