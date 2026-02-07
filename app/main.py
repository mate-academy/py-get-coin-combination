def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]
    if not isinstance(cents, int):
        raise TypeError("cents should be an integer")
    if cents < 0:
        raise ValueError("cents should be non-negative")
    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
