import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coin, expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ],
        ids=[
            "Expected 1 penny",
            "Expected 1 penny, 1 nickel",
            "Expected 2 pennies, 1 nickel, 1 dime",
            "Expected 2 quarters",
        ]
    )
    def test_get_coin_combination(
            self,
            coin: int,
            expected: list[int]
    ) -> None:
        assert get_coin_combination(coin) == expected

    @pytest.mark.parametrize(
        "cents, expected_error",
        [
            ("1", TypeError),
        ],
        ids=[
            "cents should be an integer",
        ]
    )
    def test_raising_errors_correctly(
        self,
        cents: int,
        expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
