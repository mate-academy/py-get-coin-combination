from app.coin_combination import get_coin_combination


def test_nil_coins():
    return get_coin_combination(0) == [0, 0, 0, 0]


def test_pennies():
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_nickels():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_dimes():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_all_combination():
    assert get_coin_combination(67) == [2, 1, 1, 2]
