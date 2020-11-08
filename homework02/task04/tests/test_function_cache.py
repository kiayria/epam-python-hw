import time
from collections.abc import Callable

import pytest
from function_cache.function_cache import cache


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@pytest.mark.parametrize(
    "func",
    [
        fibonacci,
    ],
)
def test_function_cache(func: Callable):
    cache_func = cache(func)
    start1 = time.time()
    val_1 = cache_func(40)
    end1 = time.time() - start1
    start2 = time.time()
    val_2 = cache_func(40)
    end2 = time.time() - start2
    print(end1, end2)
    assert val_1 is val_2
