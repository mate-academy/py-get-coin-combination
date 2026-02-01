from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("value, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3])
])
def test_combination(value: int, expected: int) -> None:
    assert get_coin_combination(value) == expected
