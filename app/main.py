def get_coin_combination(cents: int) -> list[int]:
    coins = [0, 0, 0, 0]  # pennies, nickels, dimes, quarters
    coins[3] = cents // 25
    cents %= 25
    coins[2] = cents // 10
    cents %= 10
    coins[1] = cents // 5
    cents %= 5
    coins[0] = cents
    return coins
