from app.main import get_coin_combination


def test_get_coin_combination_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_only_nickels() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_only_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_mixed_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
