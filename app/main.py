def get_coin_combination(cents: int) -> list:
    values = [25, 10, 5, 1]
    coins = [0, 0, 0, 0]

    for i in range(4):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins


print(get_coin_combination(130))
