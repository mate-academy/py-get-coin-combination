from typing import Any

import pytest

from app.main import get_coin_combination


class TestGetCoinCombinationTest:
    @pytest.mark.parametrize(
        "cent,"
        "coins", [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test should return 1-cent(coins = [1,0,0,0])"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="test should return 5-cents(coins = [0,1,0,0])"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="test should return 10-cents(coins = [0,0,1,0])"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="test should return 25-cents(coins = [0,0,0,1])"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="test should return 41-cents(coins = [1,1,1,1])"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test should return 0-cents(coins = [0,0,0,0])"
            )
        ]
    )
    def test_should_convert_cent_to_coin_combination(
            self,
            cent: int,
            coins: list
    ) -> None:

        assert get_coin_combination(cent) == coins

    @pytest.mark.parametrize(
        "cent", [
            pytest.param(
                "50",
                id="test get 'str' should raising Type Error"
            ),
            pytest.param(
                [17],
                id="test get 'list' should raising Type Error"
            ),
            pytest.param(
                {18},
                id="test get 'set' should raising Type Error"
            ),
            pytest.param(
                {1: 10},
                id="test get 'dict' should raising Type Error"
            )
        ]
    )
    def test_raising_errors_get_coin_combination(
            self,
            cent: Any,
    ) -> None:

        with pytest.raises(TypeError):
            get_coin_combination(cent)
