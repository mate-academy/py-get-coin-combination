def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins

print(get_coin_combination(0))
print(get_coin_combination(4))
print(get_coin_combination(9))
print(get_coin_combination(24))
print(get_coin_combination(67))
