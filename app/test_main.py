import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (41, [1, 1, 1, 1]),
        (37, [2, 0, 1, 1]),
        (68, [3, 1, 1, 2]),
        (57, [2, 1, 0, 2]),
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected
