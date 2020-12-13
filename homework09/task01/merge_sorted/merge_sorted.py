"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:

    with open(file_list[0]) as f1, open(file_list[1]) as f2:
        line1 = next(f1, None)
        line2 = next(f2, None)
        while line1 or line2:
            if not line1:
                yield int(line2)
                line2 = next(f2, None)
            elif not line2:
                yield int(line1)
                line1 = next(f1, None)
            else:
                if int(line1) <= int(line2):
                    yield int(line1)
                    line1 = next(f1, None)
                else:
                    yield int(line2)
                    line2 = next(f2, None)


if __name__ == "__main__":
    print(list(merge_sorted_files(["file1.txt", "file2.txt"])))
