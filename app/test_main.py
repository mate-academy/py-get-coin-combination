from app.main import get_coin_combination


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_pennies_and_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_pennies_nickels_and_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_pennies_nickels_dimes_and_quarters() -> None:
    assert get_coin_combination(67) == [2, 1, 1, 2]
