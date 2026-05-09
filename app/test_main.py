import pytest
from app import main


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_cents, convert_coin",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test_zero_cents"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test_penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="test_penny_and_nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="test_penny_nickel_dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="test_two_quarters"
            ),
            pytest.param(
                68,
                [3, 1, 1, 2],
                id="test_all_coin_types"
            )
        ]
    )
    def test_convert_correctly(self, initial_cents: int,
                               convert_coin: list) -> None:
        assert main.get_coin_combination(initial_cents) == convert_coin
