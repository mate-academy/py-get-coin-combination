def get_coin_combination(cents: int) -> list:
    if not isinstance(cents, int):
        raise TypeError("Cents must be an integer")

    if cents <= 0:
        return [0, 0, 0, 0]
    quarters = cents // 25
    remainder = cents % 25

    dimes = remainder // 10
    remainder = remainder % 10

    nickels = remainder // 5
    remainder = remainder % 5

    pennies = remainder

    return [pennies, nickels, dimes, quarters]
