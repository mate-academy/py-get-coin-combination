def get_coin_combination(cents: int) -> list[int]:
    """
    Returns the minimal number of coins for the given amount of cents.

    coins[0] = pennies (1 cent)
    coins[1] = nickels (5 cents)
    coins[2] = dimes (10 cents)
    coins[3] = quarters (25 cents)
    """
    if not isinstance(cents, int):
        raise TypeError("cents must be an integer")
    if cents < 0:
        raise ValueError("cents must be non-negative")

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    return [pennies, nickels, dimes, quarters]
