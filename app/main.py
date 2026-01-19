def get_coin_combination(cents: int) -> list[int]:
    if cents < 0:
        raise ValueError("Количество центов не может быть отрицательным.")

    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    pennies = cents % 5
    return [pennies, nickels, dimes, quarters]
