import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (2, [2, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (7, [2, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (33, [3, 1, 0, 1]),
    (50, [0, 0, 0, 2]),
    (100, [0, 0, 0, 4]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
