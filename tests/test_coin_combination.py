from app.coin_combination import get_coin_combination


def test_zero_value():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_pennies_only():
    assert get_coin_combination(2) == [2, 0, 0, 0]
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_nickel_only():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_dimes_only():
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_quarters_only():
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(500) == [0, 0, 0, 20]


def test_mix_coins():
    assert get_coin_combination(13) == [3, 0, 1, 0]
    assert get_coin_combination(35) == [0, 0, 1, 1]
    assert get_coin_combination(666) == [1, 1, 1, 26]




