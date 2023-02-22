from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_smallest_non_zero_input_value() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_for_nickels_and_pennies() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_for_dimes_nickles_and_pennies() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_for_all_types_of_coins() -> None:
    assert get_coin_combination(91) == [1, 1, 1, 3]
