from typing import List


def get_coin_combination(cents: int) -> List[int]:
    """
    Return the minimum number of US coins (pennies, nickels, dimes, quarters)
    needed to make up the given amount in cents.

    Output format: [pennies, nickels, dimes, quarters]
    """
    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    return [pennies, nickels, dimes, quarters]
