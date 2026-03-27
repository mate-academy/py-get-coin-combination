import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent,coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (1019, [4, 1, 1, 40])

    ]
)
def test_correct_amount_of_coins(cent: int, coins: list) -> None:
    assert (get_coin_combination(cent) == coins)
