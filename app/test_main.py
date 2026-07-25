from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize("cents, expected", [
        (0, [0, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (10327, [2, 0, 0, 413])
    ])
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected
