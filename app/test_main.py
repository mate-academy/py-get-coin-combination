from app.main import get_coin_combination


import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (4, [4, 0, 0, 0]),

        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),

        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (19, [4, 1, 1, 0]),

        (24, [4, 0, 2, 0]),

        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),

        (41, [1, 1, 1, 1]),  # 25 + 10 + 5 + 1
        (50, [0, 0, 0, 2]),

        (99, [4, 0, 2, 3]),  # 3*25 + 2*10 + 4*1
    ],
)
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected
