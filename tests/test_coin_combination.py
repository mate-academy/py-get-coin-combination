from app.coin_combination import get_coin_combination


def test_check_pennies_nickels_and_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_check_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_check_zero_coins():
    assert get_coin_combination(0) == [0, 0, 0, 0]
