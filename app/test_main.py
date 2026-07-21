import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="the smallest value"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="remainder of the nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="three different types of coins"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="exact quarter amount"
            )

        ]
    )
    def test_get_coin_combination_with_various_amounts(
            self,
            cents: int,
            expected_result: list[int]
    ) -> None:
        result = get_coin_combination(cents)

        assert result == expected_result
