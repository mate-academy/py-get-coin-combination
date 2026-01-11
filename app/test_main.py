from app.main import get_coin_combination


def test_no_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_any_value():
    assert get_coin_combination(43) == [3, 1, 1, 1]


def test_large_value():
    assert get_coin_combination(450124) == [4, 0, 2, 18004]
