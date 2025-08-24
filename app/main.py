def get_coin_combination(cents: int) -> list[int]:
    """
    Returns the smallest possible number of coins to represent the amount.

    coins[0] = number of pennies (1 cent)
    coins[1] = number of nickels (5 cents)
    coins[2] = number of dimes (10 cents)
    coins[3] = number of quarters (25 cents)
    """
    # Initialize coin counters: [pennies, nickels, dimes, quarters]
    coins = [0, 0, 0, 0]

    # Process from largest to smallest to minimize number of coins
    for value, index in zip(
        [25, 10, 5, 1],  # coin values
        [3, 2, 1, 0],    # their corresponding indices
    ):
        coins[index], cents = divmod(cents, value)

    return coins
