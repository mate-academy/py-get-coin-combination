from __future__ import annotations
from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny, when cents amount is 1"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="should return 1 nickel, when cents amount is 5"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="should return 1 dime, when cents amount is 10"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="should return 1 quarter, when cents amount is 25"
        ),
        pytest.param(
            43,
            [3, 1, 1, 1],
            id="another cases"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zeros, when cents amount is zero"
        )
    ]
)
def test_correctly_converted_coins(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        ("Hello there", TypeError),
        ([15], TypeError)
    ]
)
def test_should_raises_error_when_value_type_is_incorrect(
        cents: str | list,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
