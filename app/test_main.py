import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (29, [4, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (50, [0, 0, 0, 2]),
        (999, [4, 0, 2, 39])
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
