from typing import List


def get_coin_combination(cents: int) -> List[int]:
    """
    Calculate minimum coins for the given cents.
    Returns list with pennies, nickels, dimes, quarters.
    """
    pennies = cents % 5
    nickels = (cents // 5) % 2  # максимум 1 или 0 (т.к. по условию могут быть только минимальные монеты)
    dimes = (cents // 10) % 3   # максимум 2 или 0 или 1
    quarters = cents // 25

    # Но лучше считать правильно:
    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    return [pennies, nickels, dimes, quarters]
