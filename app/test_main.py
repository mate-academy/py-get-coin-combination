import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "coins, expected_list",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_correctly_combination(
            self,
            coins: int,
            expected_list: list
    ) -> None:
        assert get_coin_combination(coins) == expected_list
