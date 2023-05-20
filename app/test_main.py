from app.main import get_coin_combination


def test_return_only_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_penny_and_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_return_pennies_nickel_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_return_only_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]