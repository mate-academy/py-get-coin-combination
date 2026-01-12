import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize("cents, expected", [
        (116, [1, 1, 1, 4])
    ])
    def test_get_coin_combnination(self, cents: int, expected: list) -> None:
        result = get_coin_combination(cents)
        assert result == expected
        assert all(num >= 0 for num in result)
