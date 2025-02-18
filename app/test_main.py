import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (0, [0, 0, 0, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (60, [0, 0, 1, 2]),
        (75, [0, 0, 0, 3]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
