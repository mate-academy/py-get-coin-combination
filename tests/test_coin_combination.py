from app.coin_combination import get_coin_combination


def test_input_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_for_pennies():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_for_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_for_dimes():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_for_quarters():
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_larg_number():
    assert get_coin_combination(45148) == [3, 0, 2, 1805]
