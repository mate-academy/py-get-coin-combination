def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]
    if cents == 0:
        raise TypeError("Cents cannot be zero")

    if cents < 0:
        raise TypeError("Cents cannot be negative")

    if not isinstance(cents, int):
        raise TypeError("Cents must be an integer")

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
