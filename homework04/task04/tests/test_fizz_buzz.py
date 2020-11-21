from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz():
    """Testing fizzbuzz() with N = 20."""
    expected_result = [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizz buzz",
        "16",
        "17",
        "fizz",
        "19",
        "buzz",
    ]
    actual_result = fizzbuzz(20)
    assert actual_result == expected_result
