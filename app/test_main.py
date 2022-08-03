from app.main import get_coin_combination


def get_test_when_only_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def get_test_penny_and_nickel():
    assert get_coin_combination(7) == [2, 1, 0, 0]


def get_test_penny_and_nickel_and_dime():
    assert get_coin_combination(18) == [3, 1, 1, 0]


def get_test_quarter():
    assert get_coin_combination(75) == [0, 0, 0, 3]



