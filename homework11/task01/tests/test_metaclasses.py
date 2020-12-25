from metaclasses.metaclasses import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_enum_classes():
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"


def test_keys_amount():
    assert len(ColorsEnum) == 4
    assert len(SizesEnum) == 5
