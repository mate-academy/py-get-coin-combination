import pytest

from app.main import get_coin_combination


class TestGetCoins:
    @pytest.mark.parametrize(
        "coins,result",
        [
            (
                51, [1, 0, 0, 2]
            ),
            (
                41, [1, 1, 1, 1]
            ),
            (
                20, [0, 0, 2, 0]
            ),
            (
                16, [1, 1, 1, 0]
            ),
        ]
    )
    def test_get_coin_combination(self, coins: int, result: list[int]) -> None:
        assert get_coin_combination(coins) == result
