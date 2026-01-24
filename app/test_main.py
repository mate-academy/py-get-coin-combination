import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination_returns_expected_coins(
    cents: int, expected: list[int]
) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [0, 1, 6, 17, 41, 99])
def test_get_coin_combination_returns_valid_result_shape(cents: int) -> None:
    coins = main.get_coin_combination(cents)

    assert isinstance(coins, list)
    assert len(coins) == 4
    assert all(isinstance(coin, int) for coin in coins)
    assert all(coin >= 0 for coin in coins)

    values = [1, 5, 10, 25]
    total = sum(
        coin * value for coin, value in zip(coins, values, strict=True)
    )
    assert total == cents
