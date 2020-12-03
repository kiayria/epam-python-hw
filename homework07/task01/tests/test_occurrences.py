import pytest
from occurrences.occurrences import find_occurrences

test_data = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
        "simple_key2": [1, 1, 1],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
    "fifth": {
        "colors": ["BLUE", "BLUE", "ROYAL BLUE"],
        "jhljhl": "1",
        "complex_key": {
            "key01": "value1",
            "key02": "1",
            "key03": [1, "lot", "of", 1, {"another_nested_key": "1"}],
        },
    },
}

test_data_empty = {}


def test_occurrences_str():
    expected_result = 6
    assert find_occurrences(test_data, "RED") == expected_result


def test_occurrences_non_existent_str():
    expected_result = 0
    assert find_occurrences(test_data, "ORANGE") == expected_result


def test_occurrences_int():
    expected_result = 5
    assert find_occurrences(test_data, 1) == expected_result


def test_occurrences_non_existent_int():
    expected_result = 0
    assert find_occurrences(test_data, 0) == expected_result


def test_occurrences_negative_empty_dict():
    with pytest.raises(ValueError, match="You provided an empty dictionary."):
        find_occurrences(test_data_empty, "value")
