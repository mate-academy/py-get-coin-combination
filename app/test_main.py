from app.main import get_coin_combination


def test_get_coin_combination_1():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_6():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_17():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_50():
    assert get_coin_combination(50) == [0, 0, 0, 2]
