def get_coin_combination(cents: int) -> list:
    if cents < 0:
        raise ValueError("amount of cents cannot be negative")
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
