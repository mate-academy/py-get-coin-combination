from typing import Type

import pytest

from app.main import get_coin_combination


class TestCoinCombinationValues:
    @pytest.mark.parametrize(
        "cents, result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            result: list
    ) -> None:
        assert (get_coin_combination(cents) == result)


class TestCoinCombinationTypes:
    @pytest.mark.parametrize(
        "cents, exception",
        [
            ("1", TypeError),
            ({}, TypeError),
            ([], TypeError),
            (None, TypeError),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            exception: Type[Exception]
    ) -> None:
        with pytest.raises(exception):
            get_coin_combination(cents)
