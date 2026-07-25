from app.main import get_coin_combination


def test_return_from_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_one_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_one_penny_and_one_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_one_penny_and_one_nickel_and_one_dime():
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_get_all_coin_types():
    assert get_coin_combination(41) == [1, 1, 1, 1]
