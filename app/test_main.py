from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_data, expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="count 0 penny"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="count 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="count 1 penny + 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="count 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                66,
                [1, 1, 1, 2],
                id="count 2 quarters"
            )
        ]
    )
    def test_counting_correctly(
            self,
            initial_data: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(initial_data) == expected_result
