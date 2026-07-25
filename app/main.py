def get_coin_combination(cents: int) -> list:
    if not isinstance(cents, int):
        raise TypeError("cents must be an integer")
    if cents < 0:
        raise ValueError("cents must be >= 0")
    quarters = cents // 25
    cents = cents % 25
    dimes = cents // 10
    cents = cents % 10
    nickels = cents // 5
    cents = cents % 5
    pennies = cents
    return [pennies, nickels, dimes, quarters]
