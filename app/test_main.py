import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents,expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (11, [1, 0, 1, 0]),
    (16, [1, 1, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (66, [1, 1, 1, 2]),
    (70, [0, 0, 2, 2]),
    (421, [1, 0, 2, 16])
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
