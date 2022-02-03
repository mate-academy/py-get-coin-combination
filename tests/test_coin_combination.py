from app.coin_combination import get_coin_combination


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_all_types_coins():
    assert get_coin_combination(42) == [2, 1, 1, 1]


def test_one_coin():
    assert get_coin_combination(1) == [1, 0, 0, 0]




