import pytest

from app.main import get_coin_combination
from typing import Any


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_coins, expected_result",
        [
            pytest.param(
                1, [1, 0, 0, 0],
                id="test should return 1 penny when coin is 1"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="test should return 1 penny + 1 nickel when coin is 6"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="test should return 2 pennies + "
                   "1 nickel + 1 dime when coin is 17"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="test should return 2 quarters when coin is 50"
            ),
        ]
    )
    def test_get_coin_combination(
            self,
            initial_coins: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(
            initial_coins
        ) == expected_result

    @pytest.mark.parametrize(
        "initial_coins, expected_error",
        [
            pytest.param(
                "5",
                TypeError,
                id="should raise error when coin is 'str'"
            ),
            pytest.param(
                {},
                TypeError,
                id="should raise error when coin is 'dict'"
            ),
            pytest.param(
                [],
                TypeError,
                id="should raise error when coin is 'list'"
            ),
            pytest.param(
                (),
                TypeError,
                id="should raise error when coin is 'tuple'"
            ),
            pytest.param(
                set(),
                TypeError,
                id="should raise error when age is 'set'"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            initial_coins: Any,
            expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(initial_coins)
