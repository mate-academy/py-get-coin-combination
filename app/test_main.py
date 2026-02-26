import pytest
from app.main import get_coin_combination


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),  # boundary before nickel
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),  # boundary before dime
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (24, [4, 0, 2, 0]),  # boundary before quarter
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_coin_combinations(cents, expected):
    assert get_coin_combination(cents) == expected