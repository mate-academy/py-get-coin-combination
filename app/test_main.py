from typing import List
import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected", [
        (0, [0, 0, 0, 0]),  # 0 cents: no coins
        (1, [1, 0, 0, 0]),  # 1 cent: 1 penny
        (6, [1, 1, 0, 0]),  # 6 cents: 1 penny + 1 nickel
        (10, [0, 0, 1, 0]),  # 10 cents: 1 dime
        (17, [2, 1, 1, 0]),  # 17 cents: 2 pennies, 1 nickel, 1 dime
        (25, [0, 0, 0, 1]),  # 25 cents: 1 quarter
        (50, [0, 0, 0, 2]),  # 50 cents: 2 quarters
        (41, [1, 1, 1, 1]),  # 41 cents: 1 quarter, 1 dime, 1 nickel, 1 penny
        (99, [4, 0, 2, 3]),  # 99 cents: 3 quarters, 2 dimes, 4 pennies
    ]
)
def test_get_coin_combination_examples(cents: int, expected: List[int]) -> None:
    """Check examples from the task for get_coin_combination."""
    result = get_coin_combination(cents)
    assert result == expected


@pytest.mark.parametrize(
    "cents", [0, 1, 6, 10, 17, 25, 50, 41, 99, 123]
)
def test_get_coin_combination_structure(cents: int) -> None:
    """
    Check that:
    - the result is a list of length 4,
    - each element is a non-negative integer.
    """
    result = get_coin_combination(cents)
    assert isinstance(result, list)
    assert len(result) == 4
    for coin in result:
        assert isinstance(coin, int)
        assert coin >= 0
