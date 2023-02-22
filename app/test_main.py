from app.main import get_coin_combination


def test_zero_cents_returns_list_with_zeroes():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_cents():
    assert get_coin_combination(2) == [2, 0, 0, 0]


def test_if_5_or_more_count_nickels():
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_if_10_or_more_count_dimes():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_if_25_or_more_count_quarters():
    assert get_coin_combination(51) == [1, 0, 0, 2]
