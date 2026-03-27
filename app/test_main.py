from app.main import get_coin_combination


def test_check_number_of_pennies():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_check_number_of_nickels():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_check_number_of_dimes():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_check_number_of_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]
