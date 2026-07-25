from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination_known_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [0, 2, 30, 99, 10000])
def test_get_coin_combination_format_and_sum(cents: int) -> None:
    coins = get_coin_combination(cents)
    assert isinstance(coins, list)
    assert len(coins) == 4
    assert all(isinstance(x, int) and x >= 0 for x in coins)
    assert coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25 == cents


def test_uses_nickel_for_5() -> None:
    assert get_coin_combination(5)[1] >= 1


def test_uses_dime_for_10() -> None:
    assert get_coin_combination(10)[2] >= 1


def test_uses_quarter_for_25() -> None:
    assert get_coin_combination(25)[3] >= 1


def test_uses_quarter_for_30() -> None:
    assert get_coin_combination(30)[3] >= 1
