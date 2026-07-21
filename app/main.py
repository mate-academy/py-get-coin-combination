def get_coin_combination(cents: int) -> list:
    values = [25, 10, 5, 1]
    counts = []

    for value in values:
        counts.append(cents // value)
        cents %= value

    return [counts[3], counts[2], counts[1], counts[0]]
