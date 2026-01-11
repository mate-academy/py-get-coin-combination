from typing import List

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_expected_combinations(cents: int, expected: List[int]) -> None:
    result = get_coin_combination(cents)
    assert result == expected


@pytest.mark.parametrize("cents", [0, 1, 6, 17, 41, 99, 123, 250])
def test_structure_and_sum_correct(cents: int) -> None:
    coins = get_coin_combination(cents)
    assert isinstance(coins, list), "Result should be a list"
    assert len(coins) == 4, "Result should contain 4 items"
    assert all(isinstance(x, int) for x in coins), "Items must be int"
    assert all(x >= 0 for x in coins), "Coin counts should be non-negative"

    total = coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25
    assert total == cents, "Coin combination should sum to the original amount"


@pytest.mark.parametrize(
    "cents",
    [
        6,
        11,
        41,
        99,
    ],
)
def test_uses_multiple_coin_types_when_needed(cents: int) -> None:
    coins = get_coin_combination(cents)
    used_types = sum(1 for x in coins if x > 0)
    assert used_types >= 2
