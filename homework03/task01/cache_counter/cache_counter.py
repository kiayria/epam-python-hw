import time
from collections.abc import Callable


def cache_counter(times: int) -> Callable:
    def cache(func):
        cached_functions = dict()

        def wrapper(*args):
            func_name = func.__name__
            if func_name in cached_functions:
                if args in cached_functions[func_name]:
                    cached_functions[func_name][args]["count"] += 1
                    if cached_functions[func_name][args]["count"] <= times:
                        result = cached_functions[func_name][args]["value"]
                    else:
                        result = func(*args)
                        cached_functions[func_name][args]["count"] = 1
                        cached_functions[func_name][args]["value"] = result
                else:
                    result = func(*args)
                    cached_functions[func_name][args] = {"count": 1, "value": result}
            else:
                result = func(*args)
                cached_functions[func_name] = {args: {"count": 1, "value": result}}
            return result

        return wrapper

    return cache


@cache_counter(times=2)
def test_input():
    return input("? ")
