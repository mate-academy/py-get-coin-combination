from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (1, [1, 0, 0, 0]),  # 1 penny
            (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
            (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
            (50, [0, 0, 0, 2]),  # 2 quarters
            (99, [4, 0, 2, 3]),
            (0, [0, 0, 0, 0])
        ]
    )
    def test_return_coin_combination(
            self, cents: int, expected: list[int]) -> None:
        assert get_coin_combination(cents) == expected
