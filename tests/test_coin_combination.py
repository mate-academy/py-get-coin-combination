from app.coin_combination import get_coin_combination


def test_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_big_value():
    assert get_coin_combination(46364) == [4, 0, 1, 1854]
