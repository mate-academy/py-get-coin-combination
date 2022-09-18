from app.main import get_coin_combination


def test_should_return_zeros_when_cents_equal_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_penny_when_cents_is_one():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_nickel_when_cents_is_five():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_one_dime_when_cents_is_ten():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_one_quarter_when_cents_is_25():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_different_coins_when_cents_is_17():
    assert get_coin_combination(17) == [2, 1, 1, 0]
