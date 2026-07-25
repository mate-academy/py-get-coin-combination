import pytest
from app.main import get_coin_combination


class TestClassCurrency:
    @pytest.mark.parametrize(
        "number_of_cents,result_in_currencies",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="when entering one coin"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="checking the correct distribution of currencies"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="checking for correct distribution of quarters"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="one of each currency"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="the number of monets is zero"
            )
        ]
    )
    def test_general_function(
        self,
        number_of_cents: int,
        result_in_currencies: list
    ) -> None:
        result = get_coin_combination(number_of_cents)
        assert result == result_in_currencies
