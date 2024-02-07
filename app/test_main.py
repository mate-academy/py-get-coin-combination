import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coin, expected",
        [
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (42, [2, 1, 1, 1]),
        ],
        ids=[
            "Expected 1 penny",
            "Expected 4 penny",
            "Expected 1 penny, 1 nickel",
            "Expected 2 pennies, 1 nickel, 1 dime",
            "Expected 2 quarters",
            "Expected 2 pennies, 1 nickel, 1 dime, 1 quarters",
        ]
    )
    def test_get_coin_combination(
            self,
            coin: int,
            expected: list[int]
    ) -> None:
        result = get_coin_combination(coin)
        assert result == expected
