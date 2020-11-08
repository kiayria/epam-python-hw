import string
from typing import Any, List

import pytest
from range_function.range_function import custom_range


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        ([string.ascii_lowercase, "g"], ["a", "b", "c", "d", "e", "f"]),
        (
            [string.ascii_lowercase, "g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ([string.ascii_lowercase, "p", "g", -2], ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(args: List, expected_result: List[Any]):
    actual_result = custom_range(*args)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "args",
    [
        ([string.ascii_lowercase, "g", "p", -1]),
    ],
)
def test_input_exception(args: List):
    with pytest.raises(ValueError):
        assert custom_range(*args)
