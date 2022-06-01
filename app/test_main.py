from app.main import get_coin_combination


def test_get_coin_combination_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_one_nickel_plus():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_one_dime_plus():
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_get_coin_combination_one_quarter_plus():
    assert get_coin_combination(41) == [1, 1, 1, 1]
