from app.main import get_coin_combination


def test_should_return_all_types_of_coins():
    assert get_coin_combination(66) == [1, 1, 1, 2]


def test_combinations_less_than_100():
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(30) == [0, 1, 0, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_combinations_greater_than_100():
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(101) == [1, 0, 0, 4]
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_with_basic_cases():
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]
