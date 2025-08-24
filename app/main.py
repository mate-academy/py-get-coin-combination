from typing import List


def get_coin_combination(cents: int) -> List[int]:
    """
    Calculate the minimum number of coins needed to make the given amount in cents.
    Returns a list of counts of quarters, dimes, nickels, and pennies.
    """
    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    return [quarters, dimes, nickels, pennies]
