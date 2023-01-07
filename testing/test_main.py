from main import get_none
from main import flatten_dict


def test_get_none():
    assert get_none(1, 2) is None


def test_flatten_dict():
    assert isinstance(flatten_dict({"a": 1}), list) == True
    assert flatten_dict([{"a": 42}]) == [42]
    assert flatten_dict({"a": 42, "b": 3.14}) == [42, 3.14]
    assert flatten_dict({"a": [42, 350], "b": 3.14}) == [42, 350, 3.14]
    assert flatten_dict({"a": {"inner_a": 42, "inner_b": 350}, "b": 3.14}) == [
        42,
        350,
        3.14,
    ]
    # assert flatten_dict({"a": [{"inner_inner_a": 42}]}) == [42]
