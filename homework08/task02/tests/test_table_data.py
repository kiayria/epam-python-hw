import pytest
from table_data.table_data import TableData

presidents = TableData(database_name="example.sqlite", table_name="presidents")


def test_table_data_init():
    expected_db_name = "example.sqlite"
    expected_table = "presidents"
    assert getattr(presidents, "db") == expected_db_name
    assert getattr(presidents, "table") == expected_table


def test_table_data_len():
    n = len(presidents)
    assert n == 3


def test_table_data_access():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert presidents["Trump"] == ("Trump", 1337, "US")


def test_table_data_access_negative():
    assert presidents["Yeti"] is None
    assert presidents["Truck"] is None


def test_table_data_contains():
    existing = "Yeltsin" in presidents
    assert existing is True


def test_table_data_contains_negative():
    existing = "Yeyi" in presidents
    assert existing is False


def test_table_data_iteration():
    expected_results = ["Yeltsin", "Trump", "Big Man Tyrone"]
    assert expected_results == [president["name"] for president in presidents]
