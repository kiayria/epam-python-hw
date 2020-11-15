from unittest import mock

from cache_counter.cache_counter import cache_counter


def test_cache_counter():
    m = mock.Mock()
    m.__name__ = "foo"
    cached_func = cache_counter(times=5)(m)
    for i in range(15):
        cached_func()

    assert m.call_count == 3
