import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (9, [4, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (11, [1, 0, 1, 0]),
            (18, [3, 1, 1, 0]),
            (24, [4, 0, 2, 0]),
            (25, [0, 0, 0, 1]),
            (49, [4, 0, 2, 1]),
            (91, [1, 1, 1, 3]),
        ],
        ids=[
            "Should return 0 penny",
            "Should return 1 penny",
            "Should return 4 pennies",
            "Should return 1 nickel",
            "Should return 4 pennies and 1 nickel",
            "Should return 1 dime",
            "Should return 1 penny and 1 dime",
            "Should return 3 pennies, 1 nickel and 1 dime",
            "Should return 4 pennies and 2 dimes",
            "Should return 1 quarter",
            "Should return 4 pennies, 2 dimes and 1 quarter",
            "Should return 1 penny, 1 nickel, dime and 3 quarter"

        ]
    )
    def test_expected_result(
            self, cents: int, expected_result: list[int]
    ) -> None:

        assert get_coin_combination(cents) == expected_result
