from app.main import get_coin_combination


def test_get_coin_combination_could_return_zero_coins():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_could_return_pennies():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_could_return_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_could_return_dimes():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_coin_combination_could_return_quarters():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_could_return_coins_different_types():
    assert get_coin_combination(394) == [4, 1, 1, 15]
