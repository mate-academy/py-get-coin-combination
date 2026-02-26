import pytest
from app.main import get_coin_combination


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents, expected",
    [
        # pennies only + boundary before nickel
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),

        # nickel appears + just after
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),

        # boundary before dime + dime appears + just after
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),

        # boundary before quarter + quarter appears + just after
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),

        # mixed cases (from examples + additional)
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_coin_combinations(cents, expected):
    assert get_coin_combination(cents) == expected