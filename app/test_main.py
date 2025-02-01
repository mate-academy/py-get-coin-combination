from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_only_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_only_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_combination_quarters_and_dimes() -> None:
    assert get_coin_combination(65) == [0, 0, 1, 2]


def test_combination_all_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_large_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
