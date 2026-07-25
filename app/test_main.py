from app.main import get_coin_combination

import pytest


class TestCoins:

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
            (41, [1, 1, 1, 1]),
            (1000, [0, 0, 0, 40]),
        ],
        ids=[
            "1 penny",
            "1 penny + 1 nickel",
            "2 pennies + 1 nickel + 1 dime",
            "2 quarters",
            "4 pennies + 2 dimes + 3 quarters",
            "0 cents",
            "1 quarter",
            "1 penny + 1 nickel + 1 dime + 1 quarter",
            "40 quarters",
        ]
    )
    def test_get_coin_combination(self, cents: int, expected: [list]) -> None:
        assert get_coin_combination(cents) == expected
