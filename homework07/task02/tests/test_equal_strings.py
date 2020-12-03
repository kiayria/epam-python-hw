import pytest
from equal_strings.equal_strings import backspace_compare


def test_backspace_compare_empty_strings():
    assert backspace_compare("", "") is True


def test_backspace_compare_one_empty_string():
    assert backspace_compare("", "apple#") is False


@pytest.mark.parametrize(
    ["first", "second", "expected_result"],
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("aa##c", "#a#a#c", True),
        ("abc#c#d", "#a#c#aa#bb#d", True),
        ("ac##acdc#b", "#a#c#aac##cd#db", True),
    ],
)
def test_backspace_compare_positive(first, second, expected_result):
    actual_result = backspace_compare(first, second)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["first", "second", "expected_result"],
    [
        ("ab#c00", "ad#c#", False),
        ("a##c01#", "#a#c", False),
        ("aa##c1", "#a#1a#c#", False),
        ("abc#c#1d", "#a#c#aa#bb#d##", False),
        ("ac##acdc#1b", "#a#c#aac##cd#db#", False),
    ],
)
def test_backspace_compare_negative(first, second, expected_result):
    actual_result = backspace_compare(first, second)
    assert actual_result == expected_result
