import pytest

from app.main import get_coin_combination


class TestCoinsCombination:
    @pytest.mark.parametrize("cents,expected", [
        pytest.param(1, [1, 0, 0, 0], id="should return 1 penny"),
        pytest.param(
            6,
            [1, 1, 0, 0], id="should return 1 penny, 1 nickel"),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 2 pennies, 1 nickel, 1 dime",
        ),
        pytest.param(
            92,
            [2, 1, 1, 3],
            id="should return 2 pennies, 1 nickel, 1 dime, 3 quarters",
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return 2 quarters",
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return 1 for each coin",
        ),
    ])
    def test_coins_combination(self, cents: int, expected: list[int]) -> None:
        assert get_coin_combination(cents) == expected
