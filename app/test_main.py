from app.main import get_coin_combination


def test_get_coin_combination_single_coin() -> None:
    # Testing single coin scenarios
    assert get_coin_combination(1) == [1, 0, 0, 0]  # 1 penny
    assert get_coin_combination(5) == [0, 1, 0, 0]  # 1 nickel
    assert get_coin_combination(10) == [0, 0, 1, 0]  # 1 dime
    assert get_coin_combination(25) == [0, 0, 0, 1]  # 1 quarter


def test_get_coin_combination_mixed_coins() -> None:
    # Testing combinations of coins
    assert get_coin_combination(6) == [1, 1, 0, 0]
    # 1 penny + 1 nickel
    assert get_coin_combination(17) == [2, 1, 1, 0]
    # 2 pennies + 1 nickel + 1 dime
    assert get_coin_combination(30) == [0, 1, 0, 1]
    # 1 nickel + 1 quarter
    assert get_coin_combination(41) == [1, 1, 1, 1]
    # 1 penny + 1 nickel + 1 dime + 1 quarter


def test_get_coin_combination_large_amount() -> None:
    # Testing larger amounts with multiple coins
    assert get_coin_combination(50) == [0, 0, 0, 2]
    # 2 quarters
    assert get_coin_combination(99) == [4, 0, 2, 3]
    # 4 pennies + 2 dimes + 3 quarters


def test_get_coin_combination_zero() -> None:
    # Testing edge case: 0 cents
    assert get_coin_combination(0) == [0, 0, 0, 0]  # No coins


def test_get_coin_combination_boundary() -> None:
    # Testing boundary values
    assert get_coin_combination(24) == [4, 0, 2, 0]  # 4 pennies + 2 dimes
    assert get_coin_combination(26) == [1, 0, 0, 1]  # 1 penny + 1 quarter
