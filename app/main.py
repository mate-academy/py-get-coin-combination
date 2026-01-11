def get_coin_combination(cents: int) -> list:
    if not isinstance(cents, int):
        raise TypeError("cents must be integer!")

    if cents < 0:
        raise ValueError("value must be positive")

    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
