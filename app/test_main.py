from app.main import get_coin_combination


def test_should_return_1_penny_if_given_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1_nickel_if_given_5_cent():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_1_dime_if_given_10_cent():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_1_quarter_if_given_25_cent():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_6_coins_if_given_67_cent():
    assert get_coin_combination(67) == [2, 1, 1, 2]
