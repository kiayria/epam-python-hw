from save_original_info.save_original_info import print_result


def dummy_function(x):
    """Dummy docstring"""
    return x


def test_decorator():
    decorated = print_result(dummy_function)
    assert decorated.__name__ == "dummy_function"
    assert decorated.__doc__ == "Dummy docstring"
    assert decorated.__original_func == dummy_function
