from typing import List, Tuple

import pytest
from major_minor_elements.major_minor_elements import major_and_minor_elem


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_major_and_minor_elem(data: List[int], expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(data)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "data",
    [
        ([2, 2, 1, 1, 1, 2, 2, 1]),
        ([2, 2, 2, 2, 2]),
    ],
)
def test_input_exception(data: List[int]):
    with pytest.raises(ValueError):
        assert major_and_minor_elem(data)
