def get_coin_combination(cents: int) -> list[int]:
    values = [25, 10, 5, 1]
    res = []

    for coin in values:
        count, cents = divmod(cents, coin)
        res.append(count)

    return res[::-1]
