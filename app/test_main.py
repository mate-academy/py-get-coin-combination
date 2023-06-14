import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_coins_combination",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ],
        ids=[
            "result should be 0 coins if cents == 0",
            "result should be 1 penny if cents == 1",
            "result should be 1 penny, 1 nickel if cents == 6",
            "result should be 2 penny, 1 nickel and 1 dime if cents == 17",
            "result should be 2 quarters if cents == 50"
        ]
    )
    def test_correct_combination(
            self,
            cents: int,
            expected_coins_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_coins_combination
