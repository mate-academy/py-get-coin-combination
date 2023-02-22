import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "check 1 penny",
            "check 1 penny + 1 nickel",
            "check 2 pennies + 1 nickel + 1 dime",
            "check 2 quarters"
        ]
    )
    def test_coin_combination(
            self,
            cents: int,
            coins: list) -> None:
        assert get_coin_combination(cents) == coins
