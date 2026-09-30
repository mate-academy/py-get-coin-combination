def get_coin_combination(cents: int) -> list[int]:
    """Повертає комбінацію найменшої кількості монет для заданої суми."""
    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    return [pennies, nickels, dimes, quarters]
