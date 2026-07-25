import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        (0, [0, 0, 0, 0]),
        (25, [0, 0, 0, 1]),
        (10, [0, 0, 1, 0]),
        (5, [0, 1, 0, 0]),
        (1, [1, 0, 0, 0]),
        (41, [1, 1, 1, 1]),
        (1123, [3, 0, 2, 44]),
    ],
)
def test_coins_values(coins: int, expected: list[int]) -> None:
    assert get_coin_combination(coins) == expected


@pytest.mark.parametrize("coins", [-1])
def test_negative_values(coins: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(coins)
