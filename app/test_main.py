from app.main import get_coin_combination
import pytest


class TestCoin:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (65, [0, 1, 1, 2]),
            (98, [3, 0, 2, 3]),
            (388, [3, 0, 1, 15])
        ],
        ids=[
            "1 penny",
            "1 nickel",
            "1 dime",
            "1 quarter",
            "1 nickel, 1 dime, 2 quarters",
            "3 pennies, 2 dimes, 3 quarters",
            "3 pennies, 1 dime, 15 quarters"
        ]
    )
    def test_func_for_type_error(
            self,
            cents: str | int,
            expected: list
    ) -> None:
        assert get_coin_combination(cents) == expected
