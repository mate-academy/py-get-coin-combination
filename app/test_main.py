from app.main import get_coin_combination


def test_when_give_zero_and_return_all_zero_list():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_return_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_return_one_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_one_penny_plus_one_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_one_penny_plus_one_nickel_plus_one_dime():
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_one_penny_plus_one_nickel_plus_one_dime_plus_one_quarter():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_big_amount_of_pennies():
    assert get_coin_combination(1234) == [4, 1, 0, 49]
