from typing import Any

import pytest

from app.main import get_coin_combination


class TestCoinCombinations:
    @pytest.mark.parametrize(
        "cents, output",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test 0 value"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test only penny"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="test only nickel"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="test only dimes"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="test only quarter"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="test small value"
            ),
            pytest.param(
                3654,
                [4, 0, 0, 146],
                id="test huge value"
            ),
            pytest.param(
                39487,
                [2, 0, 1, 1579],
                id="test another huge value"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            output: list[int]
    ) -> None:
        assert get_coin_combination(cents) == output

    @pytest.mark.parametrize(
        "cents, error",
        [
            pytest.param(
                "eleven",
                TypeError,
                id="raise error when incorrect value"
            )
        ]
    )
    def test_raise_error_in_coin_combinations(
            self,
            cents: int,
            error: Any
    ) -> None:
        with pytest.raises(error):
            get_coin_combination(cents)
