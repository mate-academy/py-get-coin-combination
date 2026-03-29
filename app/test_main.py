from app.main import get_coin_combination


def test_should_return_0_when_cents_equal_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_nickels():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_dimes():
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_quarters():
    assert get_coin_combination(19) == [4, 1, 1, 0]


def test_more_than_twenty_five_cent():
    assert get_coin_combination(42) == [2, 1, 1, 1]
