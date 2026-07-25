import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (100, [0, 0, 0, 4]),
            (25, [0, 0, 0, 1]),
            (11, [1, 0, 1, 0]),
            (30, [0, 1, 0, 1])
        ]
    )
    def test_expected_values_are_correct(
        self,
        cents: int,
        coins: list[int]
    ) -> None:
        assert get_coin_combination(cents) == coins
