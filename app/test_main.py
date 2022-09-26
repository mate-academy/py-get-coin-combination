import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (16, [1, 1, 1, 0]),
            (41, [1, 1, 1, 1])
        ]
    )
    def test_correct_coins(
            self,
            cents,
            coins
    ):
        assert get_coin_combination(cents) == coins
