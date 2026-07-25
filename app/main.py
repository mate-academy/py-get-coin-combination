from typing import List


def get_coin_combination(cents: int) -> List[int]:
    values: List[int] = [1, 5, 10, 25]
    coins: List[int] = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
