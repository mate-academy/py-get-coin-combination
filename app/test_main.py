import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return 0 pennies"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return 1 penny"
            ),
            pytest.param(
                8,
                [3, 1, 0, 0],
                id="should return 3 pennies and 1 nickel"
            ),
            pytest.param(
                21,
                [1, 0, 2, 0],
                id="should return 1 penny 2 dimes"
            ),
            pytest.param(
                44,
                [4, 1, 1, 1]
            )
        ]
    )
    def test_got_coins_correctly(
        self,
        cents: int,
        expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result
