def get_coin_combination(cents: int) -> list:
    if not isinstance(cents, int) or isinstance(cents, bool):
        raise TypeError

    if cents < 0:
        return [0, 0, 0, 0]

    quarters = cents // 25
    remaining = cents % 25

    dimes = remaining // 10
    remaining = remaining % 10

    nickels = remaining // 5
    remaining = remaining % 5

    pennies = remaining

    return [pennies, nickels, dimes, quarters]
