from app.main import get_coin_combination


def test_function_can_return_different_types_of_coins() -> None:
    combination = get_coin_combination(6)
    assert combination[1] * combination[0] != 0


def test_function_can_return_not_only_pennies() -> None:
    combination = get_coin_combination(6)
    assert combination[1] != 0
