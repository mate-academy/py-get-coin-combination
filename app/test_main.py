from app import main


def test_returns_zero_coins_for_zero_cents() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_returns_only_pennies_for_small_amount() -> None:
    assert main.get_coin_combination(4) == [4, 0, 0, 0]


def test_combines_pennies_and_nickels() -> None:
    assert main.get_coin_combination(6) == [1, 1, 0, 0]


def test_combines_pennies_nickels_and_dimes() -> None:
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_uses_multiple_coin_types_with_quarters() -> None:
    assert main.get_coin_combination(41) == [1, 1, 1, 1]
