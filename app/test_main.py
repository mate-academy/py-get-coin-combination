import pytest
from app.main import get_coin_combination
from typing import List


@pytest.mark.parametrize("cents, expected_result", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),  # 1 penny
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),  # 1 penny + 1 nickels
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),  # 2 penny + 1 nickels + 1 dimes
    (24, [4, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (49, [4, 0, 2, 1]),
    (50, [0, 0, 0, 2]),  # 2 quarters
    (74, [4, 0, 2, 2]),
    (99, [4, 0, 2, 3]),
    (500, [0, 0, 0, 20]),
    (999, [4, 0, 2, 39]),
])
def test_get_coin_combination(cents: int, expected_result: List[int]) -> None:
    assert expected_result == get_coin_combination(cents), \
        (f"Expected {expected_result} for cents={cents}, "
         f" but got {get_coin_combination(cents)}")
