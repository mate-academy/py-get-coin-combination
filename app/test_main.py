from app.main import get_coin_combination


def test_get_coin_combination_for_coins() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_get_coin_combination_for_nickels() -> None:
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_get_coin_combination_for_dimes() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_get_coin_combination_for_quarters() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]
