import pytest
from count_dots.count_dots import count_dots_on_i


def test_count_dots_positive():
    actual_result = count_dots_on_i("https://example.com/")
    assert actual_result == 59


def test_count_dots_negative():
    with pytest.raises(ValueError):
        count_dots_on_i("https://example.com/faq")
