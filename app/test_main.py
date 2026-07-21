import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (41, [1, 1, 1, 1]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "should return correct value for 1 cent",
            "should return correct value for 6 cents",
            "should return correct value for 17 cents",
            "should return correct value for 41 cents",
            "should return correct value for 50 cents"
        ]
    )
    def test_convert_to_smallest_number_of_coins_correctly(
            self, cents: int, coins: list[int]
    ) -> None:

        assert get_coin_combination(cents) == coins
