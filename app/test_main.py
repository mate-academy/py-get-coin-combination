import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "should return 1 penny",
            "should return 1 penny and 1 nickel",
            "should return 2 penny, 1 nickel and 1 dime",
            "should return 2 quarters"
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  expected: list[int]) -> None:
        assert get_coin_combination(cents) == expected
