import pytest
from app.main import get_coin_combination


def minimal_coins_count(cents: int) -> int:
    """
    Helper function: calculates the minimal number of coins for a given amount.
    """
    coins = [0, 0, 0, 0]  # [pennies, nickels, dimes, quarters]
    values = [1, 5, 10, 25]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return sum(coins)


@pytest.mark.parametrize("cents", range(0, 101))
def test_get_coin_combination_minimal_coins(cents: int) -> None:
    """
    Checks that the function always returns the minimal number of coins
    for amounts 0-100.
    """
    result = get_coin_combination(cents)
    total_coins = sum(result)
    expected_min = minimal_coins_count(cents)

    assert total_coins == expected_min, (
        f"For {cents} cents, expected {expected_min} coins, "
        f"got {total_coins} coins: {result}"
    )
