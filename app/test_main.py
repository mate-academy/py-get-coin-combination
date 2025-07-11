import pytest
from app.main import get_coin_combination


test_cases = [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (2, [2, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (11, [1, 0, 1, 0]),
    (15, [0, 1, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (26, [1, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (35, [0, 0, 1, 1]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
]


@pytest.mark.parametrize("cents, expected", test_cases)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
