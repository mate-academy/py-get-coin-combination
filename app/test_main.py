import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(
                1, [1, 0, 0, 0],
                id="1 cent should return list with 1 penny and 0 other coins"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="17 cents should return list with "
                   "2 pennies, 1 nickel and 1 dime"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="50 cents should return list with "
                   "2 quarters and 0 other coins"
            ),
            pytest.param(
                0, [0, 0, 0, 0],
                id="0 coins should return list with 0"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected:
            list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected
