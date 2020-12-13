import os
import tempfile

from merge_sorted.merge_sorted import merge_sorted_files


def prepare_file(content1, content2):
    def decorate(f):
        def wrapper():
            with tempfile.NamedTemporaryFile(mode="w") as tmpfile1:
                with tempfile.NamedTemporaryFile(mode="w") as tmpfile2:
                    tmpfile1.write(content1)
                    tmpfile1.flush()
                    tmpfile2.write(content2)
                    tmpfile2.flush()
                    return f(file_path1=tmpfile1.name, file_path2=tmpfile2.name)

        return wrapper

    return decorate


@prepare_file(content1="1\n3\n5\n", content2="2\n4\n6\n")
def test_merge_sorted_line_by_line(file_path1, file_path2):
    expected_result = [1, 2, 3, 4, 5, 6]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="1\n3\n5\n", content2="7\n9\n11\n")
def test_merge_sorted_first_second(file_path1, file_path2):
    expected_result = [1, 3, 5, 7, 9, 11]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="7\n9\n11\n", content2="1\n3\n5\n")
def test_merge_sorted_second_first(file_path1, file_path2):
    expected_result = [1, 3, 5, 7, 9, 11]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="7\n9\n11\n", content2="7\n9\n11\n")
def test_merge_sorted_same_files(file_path1, file_path2):
    expected_result = [7, 7, 9, 9, 11, 11]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="", content2="7\n9\n11\n")
def test_merge_sorted_first_empty(file_path1, file_path2):
    expected_result = [7, 9, 11]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="7\n9\n11\n", content2="")
def test_merge_sorted_second_empty(file_path1, file_path2):
    expected_result = [7, 9, 11]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="", content2="")
def test_merge_sorted_both_empty(file_path1, file_path2):
    expected_result = []
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="3\n399\n1000", content2="1\n2030\n8800")
def test_merge_sorted_different_range_in_between(file_path1, file_path2):
    expected_result = [1, 3, 399, 1000, 2030, 8800]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result


@prepare_file(content1="0\n399\n1000\n1050", content2="1\n")
def test_merge_sorted_different_lengths(file_path1, file_path2):
    expected_result = [0, 1, 399, 1000, 1050]
    assert os.path.exists(file_path1)
    assert os.path.exists(file_path2)
    assert list(merge_sorted_files([file_path1, file_path2])) == expected_result
