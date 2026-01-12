from app.main import get_coin_combination


def test_if_coins_equal_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_pennies_only():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_nickels_only():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_dimes_only():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_quarters_only():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mix_coins():
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_big_coins_value():
    assert get_coin_combination(1235678) == [3, 0, 0, 49427]
