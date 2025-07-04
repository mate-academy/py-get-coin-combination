import pytest
from app.main import get_coin_combination
from typing import List


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (11, [1, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
])
def test_get_coin_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_large_value() -> None:
    result = get_coin_combination(1000)
    assert result == [0, 0, 0, 40]


def test_type_and_length() -> None:
    result = get_coin_combination(87)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) and x >= 0 for x in result)
