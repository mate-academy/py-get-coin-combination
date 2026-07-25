from app.main import get_coin_combination


def test_return_only_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_one_penny_and_one_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_return_two_pennies_one_nickel_one_dimes():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_return_one_quarters():
    assert get_coin_combination(25) == [0, 0, 0, 1]
