import pytest
from logger.logger import my_precious_logger


@pytest.mark.parametrize(
    ["text", "expected_result"],
    [
        ("OK", "OK\n"),
        ("err is OK", "err is OK\n"),
        ("erro is OK too", "erro is OK too\n"),
    ],
)
def test_my_precious_logger_stdout(text, expected_result, capsys):
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out == expected_result


@pytest.mark.parametrize(
    ["text", "expected_result"],
    [
        ("error: file not found", "error: file not found\n"),
        ("Error: file not found", "Error: file not found\n"),
    ],
)
def test_my_precious_logger_stderr(text, expected_result, capsys):
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.err == expected_result
