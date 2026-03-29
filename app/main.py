from typing import List


def get_coin_combination(cents: int) -> List[int]:
    """
    Возвращает комбинацию минимального возможного количества монет
    для данной суммы в центах.

    :param cents: количество центов
    :type cents: int
    :return: список [количество пенни, количество никелей,
                     количество даймов, количество четвертаков]
    :rtype: List[int]
    """
    if cents < 0:
        raise ValueError("Количество центов должно быть неотрицательным")

    values = (1, 5, 10, 25)
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins


if __name__ == "__main__":
    amount = int(input("Введите количество центов: "))
    combination = get_coin_combination(amount)
    print(f"Комбинация монет: {combination}")
