from app.main import get_coin_combination


def test_penn() -> None:
    coins = 1
    assert get_coin_combination(coins) == [1, 0, 0, 0]


def test_nickels() -> None:
    coins = 6
    assert get_coin_combination(coins) == [1, 1, 0, 0]


def test_dimes() -> None:
    coins = 16
    assert get_coin_combination(coins) == [1, 1, 1, 0]


def test_quarters() -> None:
    coins = 41
    assert get_coin_combination(coins) == [1, 1, 1, 1]
