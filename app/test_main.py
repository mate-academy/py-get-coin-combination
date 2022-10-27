import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, smallest_number_of_coins",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return [1, 0, 0, 0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return [1, 1, 0, 0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return [2, 1, 1, 0]"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return [0, 0, 0, 2]"
            ),
        ]
    )
    def test(self, cents: int, smallest_number_of_coins: list):
        assert get_coin_combination(cents) == smallest_number_of_coins
