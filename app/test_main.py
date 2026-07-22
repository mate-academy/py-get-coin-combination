import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_cents,expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should check 1 cent"
            ),

            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should check pennies and nickels"
            ),

            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should check pennies, nickels, dime"
            ),

            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should check quaters"
            )

        ]
    )
    def test_interpetend_cents_correctly(
            self,
            initial_cents: str,
            expected_result: list
    ) -> None:
        cent = initial_cents
        assert get_coin_combination(cent) == expected_result
