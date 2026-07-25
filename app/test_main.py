from app.main import get_coin_combination
import pytest


class TestConvertCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "1 cent should return 1 penny",
            "6 cent should return 1 penny + 1 nickel",
            "17 cents should return 2 pennies + 1 nickel + 1 dime",
            "50 cents should return 2 quarters"
        ]
    )
    def test_convert_coin_combination(
        self,
        cents: int,
        result: list
    ) -> None:
        assert get_coin_combination(cents) == result
