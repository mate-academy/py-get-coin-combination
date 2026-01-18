from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (77, [2, 0, 0, 3]),
        (80, [0, 1, 0, 3]),
        (100, [0, 0, 0, 4])
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    result = get_coin_combination(cents)
    assert result == expected
