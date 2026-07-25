from app.main import get_coin_combination


def test_should_return_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_penny_and_one_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_2_pennies_one_nickel_1_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_2_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_4_quarters():
    assert get_coin_combination(100) == [0, 0, 0, 4]
