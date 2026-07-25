def validate_cents(cents: int) -> None:
    if not isinstance(cents, int):
        raise TypeError("Parameter must be an integer.")
    if cents < 0:
        raise ValueError("Parameter must be a positive number.")


def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    validate_cents(cents)

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
