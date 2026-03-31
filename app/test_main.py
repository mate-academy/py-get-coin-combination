from app.main import get_coin_combination


def test_return_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_return_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_return_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_return_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_different_coins():
    assert get_coin_combination(67) == [2, 1, 1, 2]
