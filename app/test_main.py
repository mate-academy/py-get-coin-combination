import pytest

from app.main import get_coin_combination


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            pytest.param(0, [0, 0, 0, 0],
                         id="should_return_zeroes_if_cents_are_0"),
            pytest.param(1, [1, 0, 0, 0],
                         id="should_return_1_penny_for_1_cent"),
            pytest.param(6, [1, 1, 0, 0],
                         id="should_return_1_pennies_1_nickels_for_6_cents"),
            pytest.param(16, [1, 1, 1, 0],
                         id="should_return_three_ones_for_16_cents"),
            pytest.param(17, [2, 1, 1, 0],
                         id="should_return_2_pennies_1_nickels"
                            + "_1_dimes_for_17_cents"),
            pytest.param(41, [1, 1, 1, 1],
                         id="should_return_all_ones_for_41_cents"),
            pytest.param(25, [0, 0, 0, 1],
                         id="should_return_one_quarter_for_25_cents"),
            pytest.param(50, [0, 0, 0, 2],
                         id="should_return_two_quarters_for_50_cents"),
            pytest.param(99, [4, 0, 2, 3],
                         id="should_return_4_0_2_3_for_99_cents"),
           ]
    )
    def test_returns_correct_coins(self, cents: int, coins: list[int]) -> None:
        assert get_coin_combination(cents) == coins
