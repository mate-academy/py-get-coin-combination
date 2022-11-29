import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents_quantity,expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="function calculates correctly penny"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="function calculates correctly nickel"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="function calculates correctly dime"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="function calculates correctly quarter"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="function return list with zeroes when cent's quantity is 0"
            ),
            pytest.param(
                150,
                [0, 0, 0, 6],
                id="function return the smallest-coins-number-combination"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="function could return different type coins"
            ),
        ]
    )
    def test_function_calculations(
            self,
            cents_quantity: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(cents_quantity) == expected_result
