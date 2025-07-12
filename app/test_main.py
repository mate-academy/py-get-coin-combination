from app.main import get_coin_combination

def get_coin_combination(cents):
    """
    Return the combination of the smallest possible number of coins
    for the given amount in cents.

    Args:
        cents (int): Amount in cents (non-negative integer)

    Returns:
        list: [pennies, nickels, dimes, quarters]
    """
    # Initialize the result list
    coins = [0, 0, 0, 0]  # [pennies, nickels, dimes, quarters]

    # Start with the largest denomination (quarters = 25 cents)
    coins[3] = cents // 25  # Number of quarters
    cents = cents % 25  # Remaining cents after quarters

    # Dimes (10 cents)
    coins[2] = cents // 10  # Number of dimes
    cents = cents % 10  # Remaining cents after dimes

    # Nickels (5 cents)
    coins[1] = cents // 5  # Number of nickels
    cents = cents % 5  # Remaining cents after nickels

    # Pennies (1 cent)
    coins[0] = cents  # Remaining cents are pennies

    return coins
