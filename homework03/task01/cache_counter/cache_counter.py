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


@cache_counter(times=3)
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@cache_counter(times=2)
def test_input():
    return input("? ")


# if __name__ == '__main__':
#     for i in range(10):
#         # print(test_input())
#         start = time.time()
#         fibonacci(50)
#         print(f'{i} time: {time.time() - start}')

start = time.time()
print(fibonacci(51))
print(time.time() - start)
