from app.main import get_coin_combination

import pytest


class TestCorrectData:
    @pytest.mark.parametrize(
        "coins, expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
        ]
    )
    def test_get_reversed_list(self, coins: int, expected: list) -> None:
        assert get_coin_combination(coins) == expected
