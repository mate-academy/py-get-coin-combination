from app.coin_combination import get_coin_combination


def test_penny():
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(40) == [0, 1, 1, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_all_coins():
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(82) == [2, 1, 0, 3]  # not [2, 2, 2, 2]
