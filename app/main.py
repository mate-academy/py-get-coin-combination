def get_coin_combination(cents: int) -> list[int]:
    """
    Zwraca kombinację najmniejszej możliwej liczby monet,
    dla danej kwoty w centach.

    Format listy: [pennies (1c), nickels (5c), dimes (10c), quarters (25c)].
    """
    # Monety w kolejności od największej do najmniejszej (25c, 10c, 5c, 1c)
    values = [25, 10, 5, 1]
    # Wymagana kolejność wyniku: [pennies, nickels, dimes, quarters]
    # Odpowiadające indeksy: [0, 1, 2, 3]
    coins = [0, 0, 0, 0]

    # Quarters (25c) - indeks 3
    coins[3] = cents // values[0]
    cents %= values[0]

    # Dimes (10c) - indeks 2
    coins[2] = cents // values[1]
    cents %= values[1]

    # Nickels (5c) - indeks 1
    coins[1] = cents // values[2]
    cents %= values[2]

    # Pennies (1c) - indeks 0
    coins[0] = cents

    return coins
