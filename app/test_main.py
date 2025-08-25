import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result",
    [
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
    ],
    ids=[
        "Value for 4 penny(coins 4)",
        "Value for 1 nickel(coins 5)",
        "Value for 1 penny and 1 nickel(coins 6)",
        "Value for 1 dime(coins 10)",
        "Value for 1 penny and 1 dime(coins 11)",
        "Value for 1 quarter(coins 25)",
        "Value for 1 penny and 1 quarter(coins 26)"
    ]
)
def test_get_coin_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result
