from app.main import get_coin_combination


def test_should_add_zeros_if_integer_one():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_pennies_and_nickels():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_pennies_nickels_and_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]
