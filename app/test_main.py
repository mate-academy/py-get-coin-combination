import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (9, [4, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (15, [0, 1, 1, 0]),
            (16, [1, 1, 1, 0]),
            (17, [2, 1, 1, 0]),
            (24, [4, 0, 2, 0]),
            (26, [1, 0, 0, 1]),
            (100, [0, 0, 0, 4])
        ]
    )
    def test_should_correctly_split_cents_into_coins(
        self,
        cents: int,
        coins: list
    ) -> None:
        assert get_coin_combination(cents) == coins
