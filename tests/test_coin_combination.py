from app.coin_combination import get_coin_combination


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_non_zero():
    assert get_coin_combination(66) == [1, 1, 1, 2]


def test_only_pennies():
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_only_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_only_dimes():
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_quarters():
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
