from typing import List

import pytest
from fizzbuzz.fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    ["N", "expected_result"],
    [
        (
            20,
            [
                "1",
                "2",
                "fizz",
                "4",
                "buzz",
                "fizz",
                "7",
                "8",
                "fizz",
                "buzz",
                "11",
                "fizz",
                "13",
                "14",
                "fizz buzz",
                "16",
                "17",
                "fizz",
                "19",
                "buzz",
            ],
        ),
    ],
)
def test_fizzbuzz(N: int, expected_result: List[str]):
    actual_result = fizzbuzz(N)

    assert actual_result == expected_result
