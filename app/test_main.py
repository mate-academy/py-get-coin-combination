import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (41, [1, 1, 1, 1]),
        (16, [1, 1, 1, 0]),
        (99, [4, 0, 2, 3]),
        (6, [1, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
