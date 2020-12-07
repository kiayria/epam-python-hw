import tempfile

import pytest
from key_value.key_value import KeyValueStorage


def prepare_file(content):
    def decorate(f):
        def wrapper():
            with tempfile.NamedTemporaryFile(mode="w") as tmpfile:
                tmpfile.write(content)
                tmpfile.flush()
                return f(file_path=tmpfile.name)

        return wrapper

    return decorate


@prepare_file(content="name=kek\nlast_name=top\npower=9001\nsong=shadilay\n")
def test_key_value_storage_get_item(file_path):
    storage = KeyValueStorage(file_path)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage["power"] == 9001
    assert storage["song"] == "shadilay"


@prepare_file(content="name=kek\nlast_name=top\npower=9001\nsong=shadilay\n")
def test_key_value_storage_attributes(file_path):
    storage = KeyValueStorage(file_path)
    assert storage.name == "kek"
    assert storage.last_name == "top"
    assert storage.power == 9001
    assert storage.song == "shadilay"


@prepare_file(content="1=kek\n2=top\n3=9001\n4=shadilay\n")
def test_key_value_storage_invalid_key(file_path):
    with pytest.raises(ValueError, match="is not a valid key."):
        storage = KeyValueStorage(file_path)
