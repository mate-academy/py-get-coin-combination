from app.main import get_coin_combination


def test_return_zero_coins():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_different_coins():
    assert get_coin_combination(42) == [2, 1, 1, 1]


def test_return_smallest_possible_number_of_coins():
    assert get_coin_combination(50) == [0, 0, 0, 2]
