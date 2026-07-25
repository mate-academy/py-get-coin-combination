import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coins,expected",
        [
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (9, [4, 1, 0, 0]),
        ],
        ids=[
            "1 coin should convert into 1 penny.",
            "5 coins should convert into 1 nickel.",
            "10 coins should convert into 1 dime.",
            "25 coins should convert into 1 quarter.",
            "9 coins should convert into 4 pennys and 1 nickel."
        ]
    )
    def test_get_coin_combination(self,
                                  coins: int,
                                  expected: list
                                  ) -> None:
        assert get_coin_combination(coins) == expected
