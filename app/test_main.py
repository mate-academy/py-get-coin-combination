from app.main import get_coin_combination

import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize("cents, expected_list", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (74, [4, 0, 2, 2]),
        (133, [3, 1, 0, 5]),
        (666, [1, 1, 1, 26]),
    ])
    def test_get_coin_combination(
            self,
            cents: int,
            expected_list: list
    ) -> None:
        gcc = get_coin_combination(cents)
        assert gcc == expected_list
