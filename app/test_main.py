from app.main import get_coin_combination


def test_returns_one_penny_for_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_returns_one_nickel_for_5_cents():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_returns_one_dime_for_10_cents():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_returns_one_quarter_for_25_cents():
    assert get_coin_combination(50) == [0, 0, 0, 2]
