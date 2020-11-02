import os
from typing import List, Tuple

import pytest
from max_min.max_min import find_maximum_and_minimum


def create_temporary_txt(filename: str, data: List[int]):
    f = open(filename, "w+")
    for i in data:
        f.write(str(i) + "\n")
    f.close()
    return filename


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (create_temporary_txt("test_file0.txt", [99, 55, 22, -8, -99]), (-99, 99)),
        (create_temporary_txt("test_file1.txt", [11, 0, -5, 33]), (-5, 33)),
        (create_temporary_txt("test_file2.txt", [0, 0, 0, 0]), (0, 0)),
        (create_temporary_txt("test_file3.txt", [0]), (0, 0)),
    ],
)
def test_find_max_min(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
    os.remove(file_name)
