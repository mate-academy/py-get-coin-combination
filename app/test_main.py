from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (0, [0, 0, 0, 0]),
    (99, [4, 0, 2, 3]),
    (73, [3, 0, 2, 2]),
    (25, [0, 0, 0, 1]),
    (93, [3, 1, 1, 3]),
    (15, [0, 1, 1, 0])
])
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected
