from typing import Any, List

import pytest
from combinations.combinations import combinations


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
        (
            [[1, 2, 3], [1, 2, 3]],
            [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],
        ),
        (
            [[1, 2], [3, 4], [5, 6]],
            [
                [1, 3, 5],
                [1, 3, 6],
                [1, 4, 5],
                [1, 4, 6],
                [2, 3, 5],
                [2, 3, 6],
                [2, 4, 5],
                [2, 4, 6],
            ],
        ),
    ],
)
def test_combinations(args: List, expected_result: List[Any]):
    actual_result = combinations(*args)

    assert actual_result == expected_result
