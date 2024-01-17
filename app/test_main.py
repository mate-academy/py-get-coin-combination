from app.main import get_coin_combination


def test_get_coin_combination_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]  # 1 penny
    assert get_coin_combination(3) == [3, 0, 0, 0]  # 3 pennies
    assert get_coin_combination(10) == [10, 0, 0, 0]  # 10 pennies


def test_get_coin_combination_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]  # 1 nickel
    assert get_coin_combination(15) == [0, 3, 0, 0]  # 3 nickels


def test_get_coin_combination_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]  # 1 dime
    assert get_coin_combination(25) == [0, 0, 2, 0]  # 2 dimes


def test_get_coin_combination_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]  # 1 quarter
    assert get_coin_combination(100) == [0, 0, 0, 4]  # 4 quarters


def test_get_coin_combination_mixed() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]  # 1 penny + 1 nickel
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
