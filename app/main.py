def get_coin_combination(cents: int) -> list:
    values = [25, 10, 5, 1]
    coins = [0, 0, 0, 0]

    for i, value in enumerate(values):
        if cents >= value:
            coins[i] = cents // value
            cents %= value

    return coins
