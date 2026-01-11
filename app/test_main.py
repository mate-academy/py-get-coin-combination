import pytest
from typing import Any
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "value,result",
        [
            (1, [1, 0, 0, 0]),
            (7, [2, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (50, [0, 0, 0, 2]),
            (67, [2, 1, 1, 2])
        ]
    )
    def test_coin_combination_calculated_correctly(
            self,
            value: int,
            result: list
    ) -> None:
        assert get_coin_combination(value) == result

    @pytest.mark.parametrize(
        "value,expected_error",
        [
            ({}, TypeError),
            ("7", TypeError),
        ]
    )
    def test_raising_error_correctly(
            self,
            value: Any,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(value)
