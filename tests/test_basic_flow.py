from constants import Enums


def test_enum():
    assert Enums.Enum1 == Enums('enum1')
