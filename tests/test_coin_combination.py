import pytest

from app.coin_combination import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins_list",
        [
            (0, [0, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_get_coin_combination(self, cents, coins_list):
        assert get_coin_combination(cents) == coins_list, (
            f"Function 'get_coin_combination' should return {coins_list} "
            f"when 'cents' equals to {cents}"
        )
