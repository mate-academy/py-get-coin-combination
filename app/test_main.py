from app.main import get_coin_combination
from pytest import mark, param, raises
from typing import Any


@mark.parametrize(
    "cents,expected_result",
    [
        param(0, [0, 0, 0, 0],
              id="should return zeros if coins equal 0"),
        param(1, [1, 0, 0, 0],
              id="should return penny if coins equal 1"),
        param(6, [1, 1, 0, 0],
              id="should return penny and nickel"),
        param(16, [1, 1, 1, 0],
              id="should not return only quarters"),
        param(41, [1, 1, 1, 1],
              id="should return all coins")
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result


@mark.parametrize(
    "exception,value",
    [
        param(TypeError, "41",
              id="test_should_raises_error_when_type_of_value_is_incorrect")
    ]
)
def test_raise_exception(exception: Exception, value: Any) -> None:
    with raises(exception):
        get_coin_combination(value)
