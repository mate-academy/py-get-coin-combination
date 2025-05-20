from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:

    test_cases = [
        (0, [0, 0, 0, 0]),
        (6, [1, 1, 0, 0 ]),
        (16, [1, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (10327,[2, 0, 0, 413])
    ]
    @pytest.mark.parametrize("cents, expected", test_cases)
    def test_get_coin_combination(self, cents, expected):
        assert get_coin_combination(cents) == expected
