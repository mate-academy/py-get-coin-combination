from app.main import get_coin_combination


def test_get_coin_combination_only_with_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_only_with_dimes():
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_get_coin_combination_only_with_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_only_with_pennies():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_get_coin_combination_with_different_coins():
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(27) == [2, 0, 0, 1]
    assert get_coin_combination(41) == [1, 1, 1, 1]
