def get_coin_combination(cents: int) -> list:
    pennies = 0
    nickels = 0
    dimes = 0
    quarters = 0

    if not isinstance(cents, int) or type(cents) is bool:
        raise TypeError("Input must be an integer")
    if cents < 0:
        raise ValueError("Invalid Input")
    if cents == 0:
        return [0, 0, 0, 0]

    while cents >= 25:
        quarters += 1
        cents -= 25
    while cents >= 10:
        dimes += 1
        cents -= 10
    while cents >= 5:
        nickels += 1
        cents -= 5
    while cents > 0:
        pennies += 1
        cents -= 1

    return [pennies, nickels, dimes, quarters]
