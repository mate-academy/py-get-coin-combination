import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, number_of_coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_for_possible_combinations_of_smallest_number_of_coins(
        coins: int,
        number_of_coins: list
) -> None:
    assert get_coin_combination(coins) == number_of_coins
