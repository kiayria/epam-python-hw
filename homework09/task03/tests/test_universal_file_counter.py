import tempfile
from pathlib import Path

from universal_file_counter.universal_file_counter import universal_file_counter


def prepare_file(content1, content2):
    def decorate(f):
        def wrapper():
            with tempfile.NamedTemporaryFile(mode="w") as tmpfile1:
                with tempfile.NamedTemporaryFile(mode="w") as tmpfile2:
                    tmpfile1.write(content1)
                    tmpfile1.flush()
                    tmpfile2.write(content2)
                    tmpfile2.flush()
                    return f

        return wrapper

    return decorate


@prepare_file(content1="1\n2\n3\n4\n5\n", content2="6\n7\n8\n")
def test_universal_file_counter_no_tokenizer():
    assert universal_file_counter(Path("/tmp"), "txt") == 8


@prepare_file(content1="", content2="")
def test_universal_file_counter_no_tokenizer_empty_files():
    assert universal_file_counter(Path("/tmp"), "txt") == 0


@prepare_file(content1="not empty\n", content2="")
def test_universal_file_counter_no_tokenizer_one_empty():
    assert universal_file_counter(Path("/tmp"), "txt") == 1


@prepare_file(content1="two words\nper line\n", content2="some words to count\nyay\n")
def test_universal_file_counter_with_tokenizer():
    assert universal_file_counter(Path("/tmp"), "txt", str.split) == 9


@prepare_file(content1="", content2="")
def test_universal_file_counter_with_tokenizer_empty_files():
    assert universal_file_counter(Path("/tmp"), "txt", str.split) == 0


@prepare_file(content1="just three words", content2="")
def test_universal_file_counter_with_tokenizer_one_empty():
    assert universal_file_counter(Path("/tmp"), "txt", str.split) == 3
