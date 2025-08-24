from typing import List


def get_coin_combination(cents: int) -> List[int]:
    # Calculate the smallest number of coins for the given amount in cents
    quarters = cents // 25  # Number of quarters
    cents %= 25

    dimes = cents // 10  # Number of dimes
    cents %= 10

    nickels = cents // 5  # Number of nickels
    cents %= 5

    pennies = cents  # Remaining pennies

    return [pennies, nickels, dimes, quarters]
