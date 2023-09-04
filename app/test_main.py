import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents, coins",
        [
            (
                1,
                [1, 0, 0, 0]
            ),
            (
                6,
                [1, 1, 0, 0]
            ),
            (
                16,
                [1, 1, 1, 0]
            ),
            (
                25,
                [0, 0, 0, 1]
            )
        ]
    )
    def test_coins(self, cents: int, coins: list[int]) -> None:
        assert get_coin_combination(cents) == coins
