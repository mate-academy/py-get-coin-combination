import pytest


from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "coin,result_combination",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should be 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should be 1 penny and 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should be 2 pennies and 1 nickel and 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should be 2 quarters"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            coin: int,
            result_combination: list[int]
    ) -> None:
        assert get_coin_combination(coin) == result_combination
