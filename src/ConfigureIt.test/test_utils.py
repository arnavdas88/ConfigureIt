import pytest
from ConfigureIt.parser.utils import get_object

class DummyParameter:
    def __init__(self, param_a):
        self.param_a = param_a

    def __str__(self) -> str:
        return f"DummyParameter({self.param_a})"

class DummyClass:
    def __init__(self, param_a, param_b) -> None:
        self.param_a = param_a
        self.param_b = param_b

    def __str__(self) -> str:
        return f"DummyClass({self.param_a}, {self.param_b})"

def test_get_object():
    obj_a = get_object(
        ( "Class", {"param_a": {"Param": {"param_a": 23}}, "param_b": "HI",} ),
        {"Param": DummyParameter, "Class": DummyClass, "Function": "DummyFunction"}
    )

    obj_b = DummyClass(param_a=DummyParameter(23), param_b="HI")
    assert str(obj_a) == str(obj_b)

