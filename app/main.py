"""Module for calculating coin combinations."""

from typing import List


def get_coin_combination(cents: int) -> List[int]:
    """
    Return the smallest possible number of US coins for the given cents.

    coins[0] = number of pennies (1¢)
    coins[1] = number of nickels (5¢)
    coins[2] = number of dimes (10¢)
    coins[3] = number of quarters (25¢)

    Examples:
        >>> get_coin_combination(1)
        [1, 0, 0, 0]
        >>> get_coin_combination(6)
        [1, 1, 0, 0]
        >>> get_coin_combination(30)
        [0, 0, 3, 0]
        >>> get_coin_combination(50)
        [0, 0, 0, 2]
    """
    if cents < 0:
        raise ValueError("Cents value must be non-negative.")

    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    remaining = cents
    for idx in reversed(range(len(values))):
        coins[idx] = remaining // values[idx]
        remaining %= values[idx]

    return coins
