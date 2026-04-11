import pytest
from typing import List
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
])
def test_get_coin_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_structure_and_total() -> None:
    denominations = [1, 5, 10, 25]
    cases = [0, 1, 6, 17, 30, 37, 99, 123]
    for cents in cases:
        coins = get_coin_combination(cents)
        assert isinstance(coins, list)
        assert len(coins) == 4
        assert sum(coins[i] * denominations[i] for i in range(4)) == cents
