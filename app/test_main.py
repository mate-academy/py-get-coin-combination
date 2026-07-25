import pytest
from typing import Type

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value,result",
    [
        (
            1,
            [1, 0, 0, 0]
        ),
        (
            6,
            [1, 1, 0, 0]
        ),
        (
            17,
            [2, 1, 1, 0]
        ),
        (
            50,
            [0, 0, 0, 2]
        ),
        (
            0,
            [0, 0 , 0, 0]
        )
    ]
)
def test_get_coin_combination_correctly(
    value: int,
    result: list[int]
) -> None:
    assert get_coin_combination(value) == result
    assert len(result) == 4


@pytest.mark.parametrize(
    "value,expected_error",
    [
        pytest.param(
            -1,
            ValueError,
            id="input value must be more then 0"
        ),
        pytest.param(
            0.2,
            TypeError,
            id="input value must be 'int' type"
        ),
        pytest.param(
            "1",
            TypeError,
            id="input value must be 'int' type"
        )
    ]
)
def test_raising_error_correctly(
        value: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        if value < 0:
            raise ValueError
        elif not isinstance(value, int):
            raise TypeError
