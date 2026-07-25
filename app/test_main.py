from app.main import get_coin_combination


def _sum_cents(coins: list) -> int:
    return coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25


def test_example_sums() -> None:
    cents = 69
    coins = get_coin_combination(cents)
    assert _sum_cents(coins) == cents


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_zero_only_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_zero_only_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_zero_only_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_zero_only_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_examples() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(69) == [4, 1, 1, 2]
    assert get_coin_combination(1001) == [1, 0, 0, 40]
