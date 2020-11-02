from typing import Sequence

import pytest
from fibonacci.fib import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([], False),
        ([0], True),
        ([5], False),
        ([10], False),
        ([0, 0], False),
        ([0, 1], True),
        ([89, 144], False),
        ([0, 0, 0], False),
        ([0, 1, 1], True),
        ([377, 610, 987], False),
        ([5, 2, 7, 9, 16, 25], False),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], False),
        ([0, 1, 1, 2, 3, 5, 8, 13, 21], True),
        ([987, 1597, 2584, 4181, 6765], False),
    ],
)
def test_check_fibonacci(data: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
