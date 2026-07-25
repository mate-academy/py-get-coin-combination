import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        # Edge case: zero cents
        (0, [0, 0, 0, 0]),

        # Exact single coin values
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (43, [3, 1, 1, 1]),
        (49, [4, 0, 2, 1]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (141, [1, 1, 1, 5]),
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected
