import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coins,expected_error",
        [
            pytest.param(
                "16",
                TypeError,
                id="should raise error when coins not number"
            )
        ]
    )
    def test_raising_error_correctly(
            self,
            coins: int,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(coins)

    @pytest.mark.parametrize(
        "coins,expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="result should consists  1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="result should consists 1 penny + 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="result should consists 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="result should consists 2 quarters"
            )
        ]
    )
    def test_get_coin_combination_correctly(
            self,
            coins: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(coins) == expected_result
