import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, result_lst",
        [
            pytest.param(0, [0, 0, 0, 0], id="1 cent"),
            pytest.param(1, [1, 0, 0, 0], id="1 cent"),
            pytest.param(6, [1, 1, 0, 0], id="6 cents"),
            pytest.param(16, [1, 1, 1, 0], id="16 cents"),
            pytest.param(41, [1, 1, 1, 1], id="41 cents"),
            pytest.param(50, [0, 0, 0, 2], id="50 cents")
        ]
    )
    def test_get_combination_correctly(self, cents: int, result_lst: list):
        assert(get_coin_combination(cents) == result_lst)
        
