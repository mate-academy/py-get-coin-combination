import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "1 cents should convert into 1 penny",
            "6 cents should convert into 1 penny + 1 nickel",
            "17 cents should convert into 2 pennies + 1 nickel + 1 dime",
            "50 cents should convert into 2 quarters"
        ]
    )
    def test_get_coin_combination(self, cents: int, coins: list) -> None:
        assert get_coin_combination(cents) == coins
