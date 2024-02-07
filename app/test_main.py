import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (41, [1, 1, 1, 1]),
        ],
        ids=[
            "0 cents equal 0 penny",
            "1 cents equal 1 penny",
            "6 cents equal 1 penny and 1 nickel",
            "17 cents equal 2 penny and 1 nickel and 1 dime",
            "50 cents equal 2 quarters",
            "41 cents equal 1 penny, 1 nickel, 1 dime and 1 quarter",
        ]
    )
    def test_get_coin_comb(self,
                           cents: int,
                           coins: list) -> None:
        assert get_coin_combination(cents) == coins

    @pytest.mark.parametrize(
        "cents, error",
        [
            ("10", TypeError),
        ],
        ids=[
            "cents must be int",
        ],
    )
    def test_errors_for_not_int_values(self,
                                       cents: int,
                                       error: TypeError) -> None:
        with pytest.raises(error):
            get_coin_combination(cents)
