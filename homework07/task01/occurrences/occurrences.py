"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
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
}


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    if not tree:
        raise ValueError("You provided an empty dictionary.")
    if isinstance(tree, dict):
        for k, v in tree.items():
            counter += find_occurrences(v, element)
    elif isinstance(tree, list):
        for el in tree:
            counter += find_occurrences(el, element)
    elif tree == element:
        counter += 1
    return counter


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
