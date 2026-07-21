import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (50, [0, 0, 0, 2]),
        (17, [2, 1, 1, 0]),
        (6, [1, 1, 0, 0]),
        (4, [4, 0, 0, 0]),
        (1000, [0, 0, 0, 40]),
        (20, [0, 0, 2, 0])

    ]
)
def test_should_return_correct_coins(cents: int, coins: list[int]) -> None:
    assert get_coin_combination(cents) == coins
