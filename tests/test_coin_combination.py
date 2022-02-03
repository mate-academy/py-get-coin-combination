from app.coin_combination import get_coin_combination


def test_nil_coins():
    actual = get_coin_combination(0)
    return actual == [0, 0, 0, 0]


def test_pennies():
    actual = get_coin_combination(3)
    assert actual == [3, 0, 0, 0]


def test_nickels():
    actual = get_coin_combination(6)
    assert actual == [1, 1, 0, 0]


def test_dimes():
    actual = get_coin_combination(17)
    assert actual == [2, 1, 1, 0]


def test_quarters():
    actual = get_coin_combination(50)
    assert actual == [0, 0, 0, 2]


def test_all_combination():
    actual = get_coin_combination(67)
    assert actual == [2, 1, 1, 2]
