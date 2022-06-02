from app.main import get_coin_combination


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_coin():
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_combination():
    assert get_coin_combination(21) == [1, 0, 2, 0]
    assert get_coin_combination(75) == [0, 0, 0, 3]
    assert get_coin_combination(150) == [0, 0, 0, 6]

