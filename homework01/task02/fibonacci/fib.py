"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
import math
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    data_length = len(data)
    if data_length == 0:
        return False
    elif data_length == 1:
        return data[0] == 0
    elif data_length == 2:
        return data[0] == 0 and data[1] == 1
    else:
        if data[0] == 0 and data[1] == 1:
            for i in range(data_length - 2):
                if data[i + 2] != data[i] + data[i + 1] or data[i + 2] == 0:
                    return False
        else:
            return False
    return True
