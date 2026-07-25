import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (51, [1, 0, 0, 2])
    ],
    ids=[
        "zero_cents",
        "pennie",
        "one_nickel",
        "one_dime",
        "one_quart",
        "multiple_coin_types",
        "mixed_coins"
    ]
)
def test_get_coin_combination(coins: int, expected: list[int]) -> None:
    assert get_coin_combination(coins) == expected
