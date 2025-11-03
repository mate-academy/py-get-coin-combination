def get_coin_combination(cents: int) -> list[int]:

    if cents < 0:
        raise ValueError("Amount of cents must be non-negative")

    values = [25, 10, 5, 1]
    counts = []

    for value in values:
        count = cents // value
        counts.append(count)
        cents -= count * value

    pennies = counts[3]
    nickels = counts[2]
    dimes = counts[1]
    quarters = counts[0]

    return [pennies, nickels, dimes, quarters]
