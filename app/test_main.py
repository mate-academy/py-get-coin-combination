from app.main import get_coin_combination


def test_zeros():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_each_coin_once():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_117():
    assert get_coin_combination(117) == [2, 1, 1, 4]
