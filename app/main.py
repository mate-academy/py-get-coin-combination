"""Module for calculating coin combinations."""

from typing import List


def get_coin_combination(cents: int) -> List[int]:
    """
    Return the smallest possible number of US coins for the given cents.

    coins[0] = number of pennies (1¢)
    coins[1] = number of nickels (5¢)
    coins[2] = number of dimes (10¢)
    coins[3] = number of quarters (25¢)
    """
    if cents < 0:
        raise ValueError("Cents value must be non-negative.")

    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
