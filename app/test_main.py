from app.main import get_coin_combination


def test_should_return_penny_if_cents_lower_5():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_nickel_if_cents_equal_5():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_penny_and_nickel_if_cents_upper_5_and_lower_10():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_penny_nickel_and_dime_if_cents_upper_10_and_lower_25():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_one_quarters_if_cents_equal_25():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_two_quarters_if_cents_equal_50():
    assert get_coin_combination(50) == [0, 0, 0, 2]
