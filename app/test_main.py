from app.main import get_coin_combination


def test_return_only_pennies() -> None:
    # Для копійок менше 5 повинні бути лише pennies
    assert get_coin_combination(1) == [0, 0, 0, 1]


def test_return_only_nickels() -> None:
    # Для копійок від 5 до 9 повинні бути лише nickels
    assert get_coin_combination(5) == [0, 0, 1, 0]
    assert get_coin_combination(9) == [0, 0, 1, 4]


def test_return_only_dimes() -> None:
    # Для копійок від 10 до 24 повинні бути лише dimes
    assert get_coin_combination(10) == [0, 1, 0, 0]
    assert get_coin_combination(19) == [0, 1, 1, 4]


def test_return_only_quarters() -> None:
    # Для копійок від 25 і більше повинні бути quarters
    assert get_coin_combination(25) == [1, 0, 0, 0]
    assert get_coin_combination(99) == [3, 2, 0, 4]


def test_mixed_combinations() -> None:
    # Перевірка змішаних комбінацій
    assert get_coin_combination(41) == [1, 1, 1, 1]
