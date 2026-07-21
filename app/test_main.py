import pytest

from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_coin(coins: int, result: list[int]) -> None:
    assert get_coin_combination(coins) == result


@pytest.mark.parametrize(
    "coins",
    [
        "3",
        {1: 5},
        (3, 5, 8),
    ]
)
def test_coin_type(coins: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(coins), "Incorrect data type provided"
