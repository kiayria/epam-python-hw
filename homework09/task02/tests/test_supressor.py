import pytest
from supressor.suppressor import Suppressor, suppressor


def test_suppressor_class():
    try:
        with Suppressor(ZeroDivisionError):
            1 / 0
        print("class test passed")
    except ZeroDivisionError:
        print("class test did not pass")


def test_suppressor_class_no_exception_passed():
    try:
        with Suppressor():
            1 / 0
        print("was suppressed")
    except ZeroDivisionError:
        print("was not suppressed")


def test_suppressor_class_wrong_error():
    with pytest.raises(IndexError):
        with Suppressor(ZeroDivisionError):
            [][2]


def test_suppressor_decorated_function():
    try:
        with suppressor(ZeroDivisionError):
            1 / 0
        print("function test passed")
    except ZeroDivisionError:
        print("function did not pass")


def test_suppressor_decorated_function_no_exception_passed():
    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'passed_error'"
    ):
        with suppressor():
            1 / 0


def test_suppressor_decorated_function_wrong_error():
    with pytest.raises(IndexError):
        with suppressor(ZeroDivisionError):
            [][2]
