from app.main import get_coin_combination


def test_return_1_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_1_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_return_1_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_return_1_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_return_1_all():
    assert get_coin_combination(41) == [1, 1, 1, 1]
