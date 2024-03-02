from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coins, expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (10000, [0, 0, 0, 400]),
            (13797, [2, 0, 2, 551]),
        ],
        ids=[
            "when provided a zero cents",
            "when provided 1 cent",
            "when provided 5 cents",
            "when provided 10 cents",
            "when provided 25 cents",
            "when provided 10000 cents",
            "when provided 13797 cents",
        ]
    )
    def test_get_coin_combination_correctly(
            self,
            coins: int,
            expected: list,
    ) -> None:
        assert get_coin_combination(coins) == expected
