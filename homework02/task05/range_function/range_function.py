"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""

import string
from typing import Any, List


def custom_range(structure, a=None, b=None, step=1) -> List[Any]:
    if a and b:
        if a not in structure or b not in structure:
            raise ValueError

        start_index = structure.index(a)
        end_index = structure.index(b)
        if (end_index < start_index) != (step < 0):
            raise ValueError(
                "The index of the start position must be less than the index "
                "of the end position for positive value of step and vice versa."
            )
    elif a:
        if a not in structure:
            raise ValueError
        start_index = 0
        end_index = structure.index(a)
    else:
        start_index = 0
        end_index = len(structure)

    if not isinstance(step, int):
        raise ValueError

    return list(structure[start_index:end_index:step])
