"""We have a file that works as key-value storage, each like is
represented as key and value separated by = symbol, example:
name=kek last_name=top song_name=shadilay power=9001
Values can be strings or integer numbers. If a value can be
treated both as a number and a string, it is treated as number.
Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001
In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when
there's a line 1=something) ValueError should be raised. File size is
expected to be small, you are permitted to read it entirely into memory."""


class KeyValueStorage:
    storage = {}

    def __init__(self, file_path: str):
        with open(file_path) as fi:
            for line in fi:
                key, value = line.strip().split("=")
                try:
                    int(key)
                except ValueError:
                    try:
                        self.storage[key] = int(value)
                    except ValueError:
                        self.storage[key] = value
                else:
                    raise ValueError(f"{key} is not a valid key.")

    def __getattr__(self, key):
        return self.storage[key]

    def __getitem__(self, key):
        return self.storage[key]


if __name__ == "__main__":
    storage = KeyValueStorage("task1.txt")
    print(storage["name"])  # will be string 'kek'
    print(storage.song)  # will be 'shadilay'
    print(storage.power)  # will be integer 9001
