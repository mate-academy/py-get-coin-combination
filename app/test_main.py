import pytest
from app.main import get_coin_combination
from typing import List, Tuple

# Test cases
test_cases: List[Tuple[int, List[int]]] = [
    (-5, [0, 0, 2, -1]),
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (1348, [3, 0, 2, 53])
]


@pytest.mark.parametrize("cents, expected", test_cases)
def test_get_coin_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected
