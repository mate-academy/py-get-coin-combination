from app.main import get_coin_combination


def test_1():
    assert get_coin_combination(1) == [1, 0, 0, 0]

def test_2():
    assert get_coin_combination(6) == [1, 1, 0, 0]

def test_3():
    assert get_coin_combination(17) == [2, 1, 1, 0]

def test_4():
    assert get_coin_combination(50) == [0, 0, 0, 2]
