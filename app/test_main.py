from app.main import get_coin_combination


def test_if_cents_equal_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_1_penny_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_1_nickel_5_cent():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_1_dime_10_cent():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_1_quarter_25_cent():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_any_quantity_cents():
    assert get_coin_combination(42) == [2, 1, 1, 1]
