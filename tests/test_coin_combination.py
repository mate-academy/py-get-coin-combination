from app.coin_combination import get_coin_combination


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_all_types_coins():
    assert get_coin_combination(42) == [2, 1, 1, 1]


def test_one_coin():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_only_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_only_dimes():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_only_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]
