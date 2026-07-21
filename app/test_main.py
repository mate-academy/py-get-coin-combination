from typing import Any
import pytest
from app.main import get_coin_combination


class TestGetCoinCombination():
    @pytest.mark.parametrize(
        "cents,expected",
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
                17,
                [2, 1, 1, 0],
                id="penny, nickel, dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="quarters"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="zero"
            ),
            pytest.param(
                67,
                [2, 1, 1, 2],
                id="return different coin"
            ),
        ]
    )
    def test_get_coin_combination_correct(
            self,
            cents: int,
            expected: list) -> None:
        assert get_coin_combination(cents) == expected

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                None,
                TypeError,
                id="no arguments"
            ),
            pytest.param(
                "str",
                TypeError,
                id="not int"
            ),
        ]
    )
    def test_get_coin_combination_error(
            self,
            cents: Any,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
