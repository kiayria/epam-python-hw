from collections.abc import Callable
from unittest import mock

from function_cache.function_cache import cache


def test_function_cache():
    m = mock.Mock()
    cache_func = cache(m)
    cache_func(40)
    cache_func(40)
    assert m.call_count == 1
