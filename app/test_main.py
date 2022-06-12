from app.main import get_coin_combination


def test_should_return_0_coins_when_cents_is_0():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_only_one_coin_when_cents_equal_to_its_value():
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_different_types_of_coins():
    assert get_coin_combination(42) == [2, 1, 1, 1]
