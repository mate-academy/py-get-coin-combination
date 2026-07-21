import pytest


from app.main import get_coin_combination


class TestGetCoinCom:

    @pytest.mark.parametrize(
        "initial_cents_input, expected_results",
        [
            pytest.param(
                4, [4, 0, 0, 0],
                id="should_be_pennies_when_cents_less_than_5"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="should_be_only_nickels_when_cents_equals_to_5"
            ),
            pytest.param(
                8, [3, 1, 0, 0],
                id="should_be_pennies_and_nickels_when_less_than_10"
            ),
            pytest.param(
                20, [0, 0, 2, 0],
                id="should_be_dimes_when_cents_less_then_25_and_divided_by_10"
            ),
            pytest.param(
                18, [3, 1, 1, 0],
                id="should_be_pennies_nickels_and_dimes_when_less_than_25"
            ),
            pytest.param(
                175, [0, 0, 0, 7],
                id="should_be_only_quarters_when_divisible_by_25"
            ),
            pytest.param(
                69, [4, 1, 1, 2],
                id="should_be_all_coins_when_cents_greater_than_sum_of_coins"
            ),
            pytest.param(
                0, [0, 0, 0, 0],
                id="result_should_be_zeros_when_cents_equal_to_0"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            initial_cents_input: int,
            expected_results: list
    ) -> None:
        assert get_coin_combination(initial_cents_input) == expected_results
