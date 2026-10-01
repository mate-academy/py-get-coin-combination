import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (55, [0, 1, 0, 2]),
        (101, [1, 0, 0, 4]),
    ],
    ids=[
        "0 coin",
        "1 coin",
        "5 coins",
        "6 coins",
        "10 coins",
        "25 coins",
        "50 coins",
        "55 coins",
        "101 coins",
    ]
)
def test_get_coin_all_default_combinations(coins: int, expected: list) -> None:
    assert get_coin_combination(coins) == expected
