from unittest import mock

import pytest
from count_dots.count_dots import count_dots_on_i


class HttpResponse:
    def __init__(self, content, url=None):
        self.content = content
        self.url = url

    def read(self):
        return bytes(self.content, "utf-8")

    def decode(self):
        return self.content

    def http_error(self):
        if self.content == "404":
            raise ValueError(f"Unreachable {self.url}")


@mock.patch("urllib.request.urlopen")
def test_count_dots(mock_obj):
    mock_obj.return_value = HttpResponse("this is not real content of a page")
    result = count_dots_on_i("https://www.example.com/")
    assert result == 2


@mock.patch("urllib.request.urlopen")
def test_count_dots_negative(mock_obj):
    mock_obj.side_effect = ValueError("Unreachable https://www.example.com/faq")
    with pytest.raises(ValueError, match="Unreachable https://www.example.com/faq"):
        assert count_dots_on_i("https://www.example.com/faq")
