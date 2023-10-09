from app.main import get_coin_combination


def test_coin_is_1():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_coin_is_6():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_coin_is_17():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_coin_is_50():
    assert get_coin_combination(50) == [0, 0, 0, 2]
