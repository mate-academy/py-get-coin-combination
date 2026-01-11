import pytest
from typing import Any
from app.main import get_coin_combination


class TestReturnCoinsOfTheDifferentTypes:

    @pytest.mark.parametrize(
        "cents,coins",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="only penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="penny and nickel"
            ),
            pytest.param(
                16,
                [1, 1, 1, 0],
                id="penny and nickel and dime"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="penny and nickel and dime and quarter"
            )
        ]
    )
    def test_return_coins_of_the_different_types(
        self,
        cents: int,
        coins: int
    ) -> None:
        assert get_coin_combination(cents) == coins

    @pytest.mark.parametrize(
        "cents",
        [
            pytest.param(
                "1",
                id="cents streng"
            ),
            pytest.param(
                [],
                id="cents list"
            ),
            pytest.param(
                {},
                id="cents dict"
            ),
        ]
    )
    def test_type_of_cents(
        self,
        cents: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cents)
