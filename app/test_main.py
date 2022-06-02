from app.main import get_coin_combination


def test_zero_coins():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_penny_combination():
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickels_combination():
    assert get_coin_combination(15) == [1, 0, 0, 0]
    assert get_coin_combination(9) == [4, 0, 0, 0]


def test_dimes_combination():
    assert get_coin_combination(15) == [1, 0, 0, 0]
    assert get_coin_combination(9) == [4, 0, 0, 0]


def test_full_combination():
    assert get_coin_combination(67) == [2, 1, 1, 2]
