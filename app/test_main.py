from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(3) == [3, 0, 0, 0]
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_get_coin_combination_minimal_coins() -> None:
    # 4 pennies, not 2x2 pennies
    assert get_coin_combination(4) == [4, 0, 0, 0]
    # 2 pennies + 1 nickel, not 7 pennies
    assert get_coin_combination(7) == [2, 1, 0, 0]
    # 1 penny + 1 nickel + 1 dime, not 1 penny + 2 nickels
    assert get_coin_combination(16) == [1, 1, 1, 0]
    # 1 nickel + 1 quarter, not 3 dimes
    assert get_coin_combination(30) == [0, 1, 0, 1]
