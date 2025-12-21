def get_coin_combination(cents: int) -> list:
    if not isinstance(cents, int) or isinstance(cents, bool):
        raise TypeError("Cents must integer")

    if cents < 0:
        raise ValueError("Cents can't be a negative value")

    res = []
    for coin in (25, 10, 5, 1):
        count, cents = divmod(cents, coin)
        res.append(count)

    res.reverse()
    return res
