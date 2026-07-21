import pytest
import app.main as main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_coin_combination_examples(cents: int, expected: list[int]) -> None:
    assert main.get_coin_combination(cents) == expected


def test_return_type_and_length() -> None:
    coins = main.get_coin_combination(37)
    assert isinstance(coins, list)
    assert len(coins) == 4
    assert all(isinstance(c, int) for c in coins)
    assert all(c >= 0 for c in coins)


def test_value_reconstruction() -> None:
    for cents in [0, 1, 4, 5, 9, 10, 24, 25, 30, 99]:
        coins = main.get_coin_combination(cents)
        total = coins[0] + coins[1] * 5 + coins[2] * 10 + coins[3] * 25
        assert total == cents


def test_uses_nickel_for_5_cents() -> None:
    coins = main.get_coin_combination(5)
    assert coins[1] == 1
    assert coins[0] == 0


def test_uses_quarter_and_nickel_for_30_cents() -> None:
    coins = main.get_coin_combination(30)
    assert coins[3] == 1
    assert coins[1] == 1
    assert sum(coins) == 2
