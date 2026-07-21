from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (11, [1, 0, 1, 0]),
    (30, [0, 1, 0, 1]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (123, [3, 0, 2, 4])
])
def test_get_coin_combination(cents: int, expected: list) -> list:
    assert get_coin_combination(cents) == expected
