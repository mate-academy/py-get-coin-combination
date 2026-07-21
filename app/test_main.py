import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_coins(coins: int, expected: list[int]) -> None:
    assert get_coin_combination(coins) == expected


@pytest.mark.parametrize(
    "coins",
    [
        (-1),
        (-5),
        (-7),
    ]
)
def test_negative_numbers(coins: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(coins)


@pytest.mark.parametrize(
    "coins",
    [
        ("15"),
        ("1"),
        (None),
    ]
)
def test_invalid_types(coins: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(coins)
