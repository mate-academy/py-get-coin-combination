import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize("cents, excepted_list", [
        (0, [0, 0, 0, 0]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0,1]),
        (75, [0, 0, 0, 3])
    ])

    def test_get_coin_combination(self,
                                  cents: int,
                                  excepted_list: list
                                  ) -> None:
        assert get_coin_combination(cents) == excepted_list
