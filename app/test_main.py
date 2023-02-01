from app.main import get_coin_combination


def test_one():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_6():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_17():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_50():
    assert get_coin_combination(50) == [0, 0, 0, 2]
