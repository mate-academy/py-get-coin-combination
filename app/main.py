def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        print(coins[i])
        cents -= coins[i] * values[i]
        print(cents)

    return coins


print(get_coin_combination(3))
# print(get_coin_combination(21))
# print(get_coin_combination(31))
# print(get_coin_combination(41))
# print(get_coin_combination(51))
