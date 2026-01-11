from app.main import get_coin_combination


def test_should_return_zero_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_use_only_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_use_only_nickels_and_pennies() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_use_all_coin_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_use_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_minimum_number_of_coins() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
