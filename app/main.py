from typing import List


def get_coin_combination(cents: int) -> List[int]:
    """
    Calculate the number of quarters, dimes, nickels, and pennies
    needed to make up the given amount of cents.

    Args:
        cents (int): The total amount in cents.

    Returns:
        List[int]: A list with counts of [quarters, dimes, nickels, pennies].
    """
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    return [quarters, dimes, nickels, pennies]
