from app.main import get_coin_combination


def test_get_coin_combination_returns_one_penny_for_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_returns_penny_and_nickel_for_6_cents():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_returns_penny_nickel_dime_for_17_cents():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_returns_two_quarters_for_50_cents():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_returns_all_coin_types_for_41_cents():
    assert get_coin_combination(41) == [1, 1, 1, 1]
