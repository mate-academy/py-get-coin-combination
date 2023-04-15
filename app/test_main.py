from app.main import get_coin_combination
import pytest


class TestCoinSegregation:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="value of 0 should return list with four 0"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="value of 1 should return 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="value of more than 4 and "
                   "less than 10 should include 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="value of more than 9 should "
                   "and less than 25 should include 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="value of 50 should return 2 quarters"
            )
        ]
    )
    def test_segregating_coins(
            self,
            cents: int,
            expected_result: list
    ) -> None:
        result = get_coin_combination(cents)
        assert result == expected_result
