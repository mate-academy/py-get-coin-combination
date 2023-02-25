import pytest
from typing import Type


from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            pytest.param(0, [0, 0, 0, 0]),
            pytest.param(1, [1, 0, 0, 0]),
            pytest.param(5, [0, 1, 0, 0]),
            pytest.param(10, [0, 0, 1, 0]),
            pytest.param(25, [0, 0, 0, 1]),
            pytest.param(6, [1, 1, 0, 0]),
            pytest.param(11, [1, 0, 1, 0]),
            pytest.param(26, [1, 0, 0, 1]),
            pytest.param(49, [4, 0, 2, 1])
        ],
        ids=[
            "0 cents return [0, 0, 0, 0]",
            "1 cents returns [1, 0, 0, 0]",
            "5 cents returns [0, 1, 0, 0]",
            "10 cents returns [0, 0, 1, 0]",
            "25 cents returns [0, 0, 0, 1]",
            "6 cents returns [1, 1, 0, 0]",
            "11 cents returns [1, 0, 1, 0]",
            "26 cents returns [1, 0, 0, 1]",
            "49 cents returns [4, 0, 2, 1]"
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            coins: int
    ) -> None:
        assert get_coin_combination(cents) == coins

    @pytest.mark.parametrize(
        "cents,error",
        [
            pytest.param("1", TypeError),
        ],
        ids=["if param is not an integer raises exception"]
    )
    def test_get_coin_combination_raises_error(
            self,
            cents: int,
            error: Type[Exception]
    ) -> None:
        with pytest.raises(error):
            get_coin_combination(cents)
