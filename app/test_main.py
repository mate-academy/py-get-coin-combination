import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="Should return non-empty list"
            ),
            pytest.param(
                100156255245,
                [0, 0, 2, 4006250209],
                id="Should work with big number of cents"
            ),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ]
    )
    def test_get_coin_combination(self, cents, coins_list):
        assert get_coin_combination(cents) == coins_list, (
            f"Function 'get_coin_combination' should return {coins_list},"
            f"when 'cents' equals to {cents}"
        )
