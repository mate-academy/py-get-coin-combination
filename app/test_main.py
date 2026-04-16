import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (7, [2, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (13, [3, 0, 1, 0]),
    (15, [0, 1, 1, 0]),
    (17, [2, 1, 1, 0]),
    (20, [0, 0, 2, 0]),
    (22, [2, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (27, [2, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (33, [3, 1, 0, 1]),
    (35, [0, 0, 1, 1]),
    (50, [0, 0, 0, 2]),
    (60, [0, 0, 1, 2]),
    (99, [4, 0, 2, 3]),
    (141, [1, 1, 1, 5])
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
