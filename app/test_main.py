import pytest
from typing import Any

from app.main import get_coin_combination


class TestCorrectReturnCoins:
    @pytest.mark.parametrize(
        "how_many_cents,true_coin_value",
        [
            (-5, [0, 0, 2, -1]),
            (0, [0, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (9, [4, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (19, [4, 1, 1, 0]),
            (24, [4, 0, 2, 0]),
            (25, [0, 0, 0, 1]),
            (49, [4, 0, 2, 1])
        ],
        ids=[
            "should return 2 dime, but -1 quarter when it takes -5 cents",
            "should return a list of length 4 "
            "with values 0 when it takes 0 cents",
            "should return 4 penny when it takes 4 cents",
            "should return 1 nickel when it takes 5 cents",
            "should return 4 penny and 1 nickel when it takes 9 cents",
            "should return 1 dime when it takes 10 cents",
            "should return 4 penny, 1 nickel and"
            " 1 dime when it takes 19 cents",
            "should return 4 penny and 2 dime when it takes 24 cents",
            "should return 1 quarter when it takes 25 cents",
            "should return 4 penny, 2 dime and"
            " 1 quarter when it takes 49 cents"
        ]
    )
    def test_should_return_correct_values(
            self,
            how_many_cents: int,
            true_coin_value: list
    ) -> None:
        assert get_coin_combination(how_many_cents) == true_coin_value

    @pytest.mark.parametrize(
        "how_many_cents,expected_error",
        [
            ("20", TypeError),
        ],
        ids=[
            "should raise a TypeError when it accepts string values",
        ]
    )
    def test_should_raise_error_when_takes_string_values(
            self,
            how_many_cents: int,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(how_many_cents)
