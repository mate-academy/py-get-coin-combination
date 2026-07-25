from app.main import get_coin_combination
import pytest


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cent, expected",
        [
            (0, [0, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (9, [4, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (49, [4, 0, 2, 1]),
            (50, [0, 0, 0, 2]),
        ],
        ids=[
            "0 coin should return 0",
            "4 coin should return 4 cent",
            "5 coin should return 1 nickel",
            "6 coin should return 1 nickel and 1 cent",
            "9 coin should return 1 nickel and 4 cent",
            "10 coin should return 1 dime",
            "49 coin should return 1 quarter, 2 dime and 4 cent",
            "50 coin should return 2 quarter",
        ]
    )
    def test_combination_coins(self, cent: int, expected: list) -> None:
        assert get_coin_combination(cent) == expected
