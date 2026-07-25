import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        'cents_taken, combination_received',
        [
            pytest.param(1, [1, 0, 0, 0],
                         id="should return one penny"),
            pytest.param(6, [1, 1, 0, 0],
                         id="should return 1 penny and 1 nickel"),
            pytest.param(17, [2, 1, 1, 0],
                         id="should return 2 penny, 1 nickel and 1 dime"),
            pytest.param(50, [0, 0, 0, 2],
                         id="should return 2 quarters"),
            pytest.param(51, [1, 0, 0, 2],
                         id="should return 2 quarters and 1 penny")
        ]
    )
    def test_should_return_smallest_number_of_coins(self,
                                                    cents_taken,
                                                    combination_received):

        assert get_coin_combination(cents_taken) == combination_received
