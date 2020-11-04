from typing import List

import pytest
from sum_of_four.sum_of_four import check_sum_of_four


@pytest.mark.parametrize(
    ["listA", "listB", "listC", "listD", "expected_result"],
    [
        ([0], [0], [0], [0], 1),
        ([1], [1], [1], [1], 0),
        ([0, 2], [1, 2], [3, -2], [4, -2], 1),
        ([0, 2, 3], [1, 2, 3], [-3, -2, 0], [4, -2, -3], 10),
    ],
)
def test_check_sum_of_four(
    listA: List[int],
    listB: List[int],
    listC: List[int],
    listD: List[int],
    expected_result: int,
):
    actual_result = check_sum_of_four(listA, listB, listC, listD)

    assert actual_result == expected_result
