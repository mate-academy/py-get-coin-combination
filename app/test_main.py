import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "coins,result",
        [
            pytest.param(
                1, [1, 0, 0, 0],
                id="should return 1 penny from 1 cent"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="should return 1 penny and 1 nickel from 6 cent"
            ),
            pytest.param(
                16, [1, 1, 1, 0],
                id="should return 1 penny, 1 nickel and 1 dime from 16 cent"
            ),
            pytest.param(
                41, [1, 1, 1, 1],
                id="should return [1, 1, 1, 1] from 41 cent"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="should return 2  quarters from 50 cents"
            )
        ]
    )
    def test_should_return_correct_combination(
            self,
            coins: int,
            result: list
    ) -> None:
        assert get_coin_combination(coins) == result
