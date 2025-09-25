def get_coin_combination(cents: int) -> list[int]:
    if not isinstance(cents, int):
        raise TypeError("Input must be an integer")
    if cents < 0:
        raise ValueError("Input must be non-negative")

    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    return [pennies, nickels, dimes, quarters]

