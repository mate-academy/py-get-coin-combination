def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    if isinstance(cents, str):
        raise TypeError  
    if cents < 0:
        raise ValueError
    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins

print(get_coin_combination(0))
print(get_coin_combination(1))
print(get_coin_combination(5))
print(get_coin_combination(10))
print(get_coin_combination(25))
print(get_coin_combination(26))
print(get_coin_combination(30))
print(get_coin_combination(35))
print(get_coin_combination(40))
print(get_coin_combination(41))
print(get_coin_combination(-5))
print(get_coin_combination("ab"))
