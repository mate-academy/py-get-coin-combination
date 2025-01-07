def get_coin_combination(amount: int) -> list[int]:
    coins = [1, 5, 10, 25]
    result = [0, 0, 0, 0]

    for i in range(len(coins) - 1, -1, -1):
        result[i] = amount // coins[i]
        amount %= coins[i]

    return result
