from app.main import get_coin_combination


import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="1 cent should be equal only 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="6 cents should be equal 1 penny and 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="17 cents should be equal 2 pennies 1 nickel 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="50 cents should be equal 2 quarters"
            )
        ]
    )
    def test_get_coin_combination_correctly(
            self,
            cents: int,
            result: list
    ) -> None:
        assert get_coin_combination(cents) == result

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                "172",
                TypeError,
                id="should raise error on incorrect data"
            )
        ]
    )
    def test_raising_get_coin_combination_correctly(
            self,
            cents: any,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
