"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, *args):
        self.passed_error = args

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.passed_error)


@contextmanager
def suppressor(passed_error):
    try:
        yield
    except passed_error:
        pass


if __name__ == "__main__":
    with Suppressor(IndexError):
        [][2]
    print("It works.")

    with suppressor(IndexError):
        [][2]
    print("It also works.")
