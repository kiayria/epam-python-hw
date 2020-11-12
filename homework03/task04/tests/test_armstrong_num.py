import pytest
from armstrong_num.armstrong_num import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (9, True),
        (153, True),
        (10, False),
        (0, False),
    ],
)
def test_is_armstrong(number: int, expected_result: bool):
    actual_result = is_armstrong(number)

    assert actual_result == expected_result
