import pytest
from app.main import get_coin_combination


class TestCoins:

    @pytest.mark.parametrize("cents, coins",
                             [
                                 (0, [0, 0, 0, 0]),
                                 (1, [1, 0, 0, 0]),
                                 (5, [0, 1, 0, 0]),
                                 (10, [0, 0, 1, 0]),
                                 (25, [0, 0, 0, 1]),
                                 (6, [1, 1, 0, 0]),
                                 (17, [2, 1, 1, 0]),
                                 (50, [0, 0, 0, 2]),
                                 (100, [0, 0, 0, 4]),
                                 (142, [2, 1, 1, 5])
                             ])
    def test_get_coin_combination(self, cents: int, coins: int) -> None:
        assert get_coin_combination(cents) == coins
