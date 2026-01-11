import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (18, [3, 1, 1, 0]),
        (79, [4, 0, 0, 3])
    ],
    ids=[
        "zero coins",
        "cent",
        "cent and nickel",
        "cent, nickel and dime",
        "cent and quarter"
    ]
)
def test_should_calculate_coins_combinations_correctly(
        coins: int,
        combination: list[int]
) -> None:
    assert get_coin_combination(coins) == combination
