import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents, expected_coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "1 penny",
            "1 penny + 1 nickel",
            "2 pennies + 1 nickel + 1 dime",
            "2 quarters"
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_coins: list
    ) -> None:
        assert get_coin_combination(cents) == expected_coins
