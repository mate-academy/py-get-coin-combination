from app.main import get_coin_combination


def test_cents_equal_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_gives_only_pennies():
    assert get_coin_combination(2) == [2, 0, 0, 0]


def test_gives_only_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_gives_only_dimes():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_gives_only_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_simple_mixed():
    assert get_coin_combination(67) == [2, 1, 1, 2]


def test_with_big_integer():
    assert get_coin_combination(2473) == [3, 0, 2, 98]
