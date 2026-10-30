from app import main
import pytest


class TestCoins():

    @pytest.mark.parametrize(
        "coins,expected",
        [
            (0, [0, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (41, [1, 1, 1, 1]),
            (1000, [0, 0, 0, 40]),

        ])
    def test_coins(self, coins: int, expected: list) -> None:
        assert main.get_coin_combination(coins) == expected
