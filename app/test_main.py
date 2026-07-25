import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents,expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (524, [4, 0, 2, 20])
        ],
        ids=[
            "1 cent == 1 penn.",
            "6 cents == 1 penny and 1 nickels.",
            "17 cents == 2 penny, 1 nickels and 1 dimes.",
            "50 cents == 2 quarters.",
            "524 cents == 4 penny, 2 dimes and 20 quarters."
        ]
    )
    def test_(self, cents: int, expected: list[int]) -> None:
        assert get_coin_combination(cents) == expected
