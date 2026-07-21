def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    if cents is None:
        raise TypeError("Cents amount cannot be empty")
    if not isinstance(cents, int):
        raise TypeError("Wrong type for 'cents'")
    if int(cents) < 0:
        raise ValueError("Cents amount cannot be negative")

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
