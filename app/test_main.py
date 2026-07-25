from app.main import get_coin_combination


def test_zero_cents_returns_no_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies_used_when_less_than_nickel() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickel_used_instead_of_five_pennies() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_dime_used_instead_of_two_nickels() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_quarter_used_for_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_combination_uses_minimum_number_of_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_result_is_list_of_four_elements() -> None:
    result = get_coin_combination(42)
    assert isinstance(result, list)
    assert len(result) == 4
