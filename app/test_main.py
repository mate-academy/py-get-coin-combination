import pytest
from app.main import get_coin_combination
from typing import Any


class TestCoinCombination:

    @pytest.mark.parametrize(
        "amount,expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return a list len equal to 4"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return 1 penny when amount is 1"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return 1 penny + 1 nickel when amount is 6"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id=("should return 2 pennies + 1 nickel + 1 dime"
                    " when amount is 17")
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return 2 quarters when amount is 50"
            ),
        ]
    )
    def test_give_coins_correctly(
            self,
            amount: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(amount) == expected_result

    @pytest.mark.parametrize(
        "amount,expected_error",
        [
            pytest.param("14",
                         TypeError,
                         id="should raise error when data type is not int")
        ]
    )
    def test_raise_errors_correctly(
            self,
            amount: int,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(amount)
