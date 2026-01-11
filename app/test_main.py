import pytest
from typing import List
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (101, [1, 0, 0, 4]),
])
def test_get_coin_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_large_amount() -> None:
    result = get_coin_combination(9999)
    assert sum(result[i] * [1, 5, 10, 25][i] for i in range(4)) == 9999
    assert result[3] == 399
    assert result[2] == 2
    assert result[1] == 0
    assert result[0] == 4
