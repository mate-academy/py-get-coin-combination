import pytest
from typing import Any

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "Should return [1, 0, 0, 0] when cents are 1",
            "Should return [1, 1, 0, 0] when cents are 6",
            "Should return [2, 1, 1, 0] when cents are 17",
            "Should return [0, 0, 0, 2] when cents are 50"
        ]
    )
    def test_result_of_coins(
        self,
        cents: int,
        coins: list
    ) -> None:
        assert (
            get_coin_combination(cents) == coins
        ), "Should return list of coins combination"

    @pytest.mark.parametrize(
        "cents, expected_error",
        [
            ("1", TypeError),
            ([2], TypeError),
            ((2,), TypeError),
            ({2}, TypeError),
        ],
        ids=[
            "Raises TypeError when value is string",
            "Raises TypeError when value is list",
            "Raises TypeError when value is tuple",
            "Raises TypeError when value is set",
        ]
    )
    def test_raising_errors_correctly(
        self,
        cents: Any,
        expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
