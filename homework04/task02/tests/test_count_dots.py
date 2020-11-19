from unittest.mock import patch

from count_dots.count_dots import count_dots_on_i


class HttpResponse:
    def __init__(self, content):
        self.content = content

    def read(self):
        return bytes(self.content, "utf-8")

    def decode(self):
        return self.content


@patch("urllib.request.urlopen")
def test_count_dots(mock_obj):
    mock_obj.return_value = HttpResponse("this is not real content of a page")
    result = count_dots_on_i("https://www.example.com/")
    assert result == 2
