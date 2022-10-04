def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins


print(get_coin_combination(1)) == [1, 0, 0, 0]  # 1 penny
print(get_coin_combination(6)) == [1, 1, 0, 0]  # 1 penny + 1 nickel
print(get_coin_combination(17)) == [2, 1, 1, 0]   # 2 pennies + 1 nickel + 1 dime
print(get_coin_combination(50)) #== [0, 0, 0, 2]   # 2 quarters