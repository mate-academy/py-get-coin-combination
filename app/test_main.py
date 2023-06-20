import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "input_cents,output_coins",
        [
            (25, [0, 0, 0, 1]),
            (10, [0, 0, 1, 0]),
            (5, [0, 1, 0, 0]),
            (1, [1, 0, 0, 0]),
            (41, [1, 1, 1, 1]),
            (82, [2, 1, 0, 3])
        ]
    )
    def test_should_calculate_smallest_possible_number_of_coins(
            self,
            input_cents,
            output_coins
    ) -> None:
        assert get_coin_combination(input_cents) == output_coins
