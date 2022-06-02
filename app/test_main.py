from app.main import get_coin_combination


def test_1_coin():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_even_coins():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_odd_coins():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_big_amount():
    assert get_coin_combination(50) == [0, 0, 0, 2]
