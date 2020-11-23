import os
import tempfile

import pytest
from read_file.read_file import read_magic_number


def prepare_file(content):
    def decorate(f):
        def wrapper():
            with tempfile.NamedTemporaryFile(mode="w") as tmpfile:
                tmpfile.write(content)
                tmpfile.flush()
                return f(file_path=tmpfile.name)

        return wrapper

    return decorate


@prepare_file(content="1\n2\n3")
def test_read_magic_number_positive_lower_boundary(file_path):
    """Testing read_magic_number() with a number that belongs to the interval"""
    assert os.path.exists(file_path)
    assert read_magic_number(file_path) is True


@prepare_file(content="2\n1\n3")
def test_read_magic_number_positive_upper_boundary(file_path):
    """Testing read_magic_number() with a number that belongs to the interval"""
    assert os.path.exists(file_path)
    assert read_magic_number(file_path) is True


@prepare_file(content="0\n1\n3")
def test_read_magic_number_negative_lower_boundary(file_path):
    """Testing read_magic_number() with a number that does not belong to the interval"""
    assert os.path.exists(file_path)
    assert read_magic_number(file_path) is False


@prepare_file(content="3\n1\n3")
def test_read_magic_number_negative_upper_boundary(file_path):
    """Testing read_magic_number() with a number that does not belong to the interval"""
    assert os.path.exists(file_path)
    assert read_magic_number(file_path) is False


@prepare_file(content="Text")
def test_read_magic_number_exception_not_a_number(file_path):
    with pytest.raises(ValueError):
        read_magic_number(file_path)


@prepare_file(content="")
def test_read_magic_number_exception_empty_file(file_path):
    with pytest.raises(ValueError):
        read_magic_number(file_path)


def test_read_magic_number_path():
    with pytest.raises(ValueError, match="Such file or directory does not exist."):
        read_magic_number("not_a_test_file.txt")
