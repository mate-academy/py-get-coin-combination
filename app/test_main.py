import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (0, [0, 0, 0, 0]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (41, [1, 1, 1, 1]),
    (63, [3, 0, 1, 2]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
