from typing import Dict, List

import pytest
from filter.filter import make_filter


def test_filter_output_first():
    """
    Test input: name="Bill", last_name="Gilbert"
    Expecting the first dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual_result = make_filter(name="Bill", last_name="Gilbert").apply(data)
    expected_result = [data[0]]
    assert actual_result == expected_result


def test_filter_one_key():
    """
    Testing with one key.
    Test input: last_name="Gilbert"
    Expecting the first dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual_result = make_filter(last_name="Gilbert").apply(data)
    expected_result = [data[0]]
    assert actual_result == expected_result


def test_filter_output_second():
    """
    Test input: name="polly", type="bird"
    Expecting the second dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual_result = make_filter(name="polly", type="bird").apply(data)
    expected_result = [data[1]]
    assert actual_result == expected_result


def test_filter_one_key_second():
    """
    Testing with one key
    Test input: kind="parrot"
    Expecting the second dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual_result = make_filter(kind="parrot").apply(data)
    expected_result = [data[1]]
    assert actual_result == expected_result


def test_filter_output_third():
    """
    Testing with almost identical dictionaries.
    Test input: name="billy", type="bird"
    Expecting the third dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
        {"is_dead": False, "kind": "parrot", "type": "bird", "name": "billy"},
    ]

    actual_result = make_filter(name="billy", type="bird").apply(data)
    expected_result = [data[2]]
    assert actual_result == expected_result
