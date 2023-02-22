import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test for 1 cent should return [1, 0, 0, 0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="test for 1 penny + 1 nickel should return [1, 1, 0, 0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="test for 2 pennies, 1 nickel, 1 dime return [2, 1, 1, 0]"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="test for 2 quarters should return [0, 0, 0, 2]"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test for zero penny should return [0, 0, 0, 0]"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            result: list
    ) -> None:
        assert get_coin_combination(cents) == result
