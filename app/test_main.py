import pytest

from app.main import get_coin_combination


class TestCoin:
    @pytest.mark.parametrize("cents, expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ])
    def test_get_coin_combination(self, cents, expected):
        assert get_coin_combination(cents) == expected

