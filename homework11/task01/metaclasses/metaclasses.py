"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(mcs, cls, bases, class_dict):
        key = "_" + cls + "__keys"
        keys_tuple = class_dict[key]
        del class_dict[key]
        for i in keys_tuple:
            class_dict[i] = i
        object_attrs = set(dir(type(cls, (object,), {})))
        simple_enum_cls = super().__new__(mcs, cls, bases, class_dict)
        simple_enum_cls._member_names_ = set(class_dict.keys()) - object_attrs
        non_members = set()
        for attr in simple_enum_cls._member_names_:
            if attr.startswith("_") and attr.endswith("_"):
                non_members.add(attr)
            else:
                setattr(simple_enum_cls, attr, attr)

        simple_enum_cls._member_names_.difference_update(non_members)

        return simple_enum_cls

    def __getitem__(cls, key):
        return getattr(cls, key.upper())

    def __iter__(cls):
        return (name for name in cls._member_names_)

    def __len__(cls):
        return len(cls._member_names_)


if __name__ == "__main__":

    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
