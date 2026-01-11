import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_coins",
        (
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (41, [1, 1, 1, 1]),
            (1016, [1, 1, 1, 40])
        ),
        ids=(
            "should work correctly with less than 5 cents",
            "should work correctly with 5 cents",
            "should work correctly with 10 cents",
            "should work correctly with 25 cents",
            "should work correctly with 41 cents",
            "should word correctly with bigger value"
        )
    )
    def test_returns_coins_correctly(
            self,
            cents: int,
            expected_coins: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_coins
