from app.main import get_coin_combination


import pytest


@pytest.mark.parametrize("coin, result", [
    (0, [0, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (41, [1, 1, 1, 1]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4])
])
def test_get_coin_combination(coin: int, result: list) -> None:
    assert get_coin_combination(coin) == result


def test_not_only_pennies() -> None:
    assert get_coin_combination(5) != [5, 0, 0, 0]


def test_returns_multiple_coin_types() -> None:
    coins = get_coin_combination(17)
    assert sum(1 for c in coins if c > 0) > 1
