import pytest
from app.main import get_coin_combination


class TestCoinCombinations:
    @pytest.mark.parametrize("cents, expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (99999, [4, 0, 2, 3999]),
    ])
    def test_get_coin_combination(
        self,
        cents: int,
        expected: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected
