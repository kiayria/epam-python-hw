from typing import List

import pytest
from text_manipulaion.text_manipulation import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (
            "test_data/test01.txt",
            [
                "abcdefghijklmnopqrstuvwxyz",
                "abcdefghijklmnopqrstuvwxy",
                "abcdefghijklmnopqrstuvwx",
                "abcdefghijklmnopqrstuvw",
                "abcdefghijklmnopqrstuv",
                "abcdefghijklmnopqrstu",
                "abcdefghijklmnopqrst",
                "abcdefghijklmnopqrs",
                "abcdefghijklmnopqr",
                "abcdefghijklmnopq",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("test_data/test02.txt", "Y"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    actual_result = get_rarest_char(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("test_data/test03.txt", 60),
    ],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    actual_result = count_punctuation_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("test_data/test04.txt", 97),
    ],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    actual_result = count_non_ascii_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("test_data/test05.txt", "Ф"),
    ],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: int):
    actual_result = get_most_common_non_ascii_char(file_path)

    assert actual_result == expected_result
