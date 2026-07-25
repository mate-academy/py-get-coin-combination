from app.main import get_coin_combination


def test_cents_equal_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_1_cent_equal_1_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_5_cents_equal_1_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_10_cents_equal_1_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_25_cents_equal_1_quarter():
    assert get_coin_combination(50) == [0, 0, 0, 2]
