import os

import pytest
from read_file.read_file import read_magic_number


@pytest.fixture
def setup():
    temp_file = open("test_data.txt", "w")
    yield
    temp_file.close()
    os.remove("test_data.txt")


@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize(
    "numbers",
    [
        1,
        2.5,
        2.99,
    ],
)
def test_read_magic_number_positive(numbers):
    with open("test_data.txt", "w") as f:
        f.write(f"{numbers}\n")
    path = os.path.join(os.path.dirname(__file__), "test_data.txt")
    assert read_magic_number(path) is True


@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize(
    "numbers",
    [
        0,
        0.99,
        3,
    ],
)
def test_read_magic_number_negative(numbers):
    with open("test_data.txt", "w") as f:
        f.write(f"{numbers}\n")
    path = os.path.join(os.path.dirname(__file__), "test_data.txt")
    assert read_magic_number(path) is False


@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize(
    "text",
    [
        "not a number",
        "8-xxx",
    ],
)
def test_read_magic_number_exception(text):
    with open("test_data.txt", "w") as f:
        f.write(f"{text}\n")
    path = os.path.join(os.path.dirname(__file__), "test_data.txt")
    with pytest.raises(ValueError):
        read_magic_number(path)


def test_read_magic_number_path():
    with pytest.raises(ValueError, match="Such file or directory does not exist."):
        read_magic_number("not_a_test_file.txt")
