import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="if equal to 0 coins"
            ),
            pytest.param(
                2,
                [2, 0, 0, 0],
                id="if less than 5 coins"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="if equal to 5 coins"
            ),
            pytest.param(
                9,
                [4, 1, 0, 0],
                id="if between 5 and 10 coins"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="if equal to 10 coins"
            ),
            pytest.param(
                14,
                [4, 0, 1, 0],
                id="if between 10 and 15 coins"
            ),
            pytest.param(
                18,
                [3, 1, 1, 0],
                id="if between 15 and 20 coins"
            ),
            pytest.param(
                20,
                [0, 0, 2, 0],
                id="if equal to 20 coins"
            ),
            pytest.param(
                23,
                [3, 0, 2, 0],
                id="if between 20 and 25 coins"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="if equal to 25 coins"
            ),
            pytest.param(
                100,
                [0, 0, 0, 4],
                id="if greater than 25 coins and "
                   "denominator is equal to 25"
            ),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result
