from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coin_combination, expected",
        [
            (50, [0, 0, 0, 2]),
            (17, [2, 1, 1, 0]),
            (6, [1, 1, 0, 0]),
            (1, [1, 0, 0, 0]),

            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
        ],
        ids=[
            "50 cents",
            "17 cents",
            "6 cents",
            "1 cent",
            "only pennies",
            "only nickels",
            "only dimes",
            "only quarters",
        ]
    )
    def test_get_coin_combination(
            self,
            coin_combination: int,
            expected: list[int],
    ) -> None:
        assert get_coin_combination(coin_combination) == expected
