from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coins, expected",
        [
            pytest.param(
                1,
                [1, 0, 0, 0]
            ),
            pytest.param(
                6,
                [1, 1, 0, 0]
            ),
            pytest.param(
                17,
                [2, 1, 1, 0]
            ),
            pytest.param(
                50,
                [0, 0, 0, 2]
            )
        ]
    )
    def test_get_coin_combination(
            self,
            coins: int,
            expected: list
    ) -> None:
        assert get_coin_combination(coins) == expected
