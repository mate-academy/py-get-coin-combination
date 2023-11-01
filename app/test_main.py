import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(0, [0, 0, 0, 0], id="should return zero"),
            pytest.param(5, [0, 1, 0, 0], id="should return 1 nickel"),
            pytest.param(
                11,
                [1, 0, 1, 0],
                id="should return 1 pennies + 1 dime"),
            pytest.param(1, [1, 0, 0, 0], id="should return 1 penny"),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return 1 penny + 1 nickel"),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(50, [0, 0, 0, 2], id="should return 2 quarters"),
            pytest.param(20, [0, 0, 2, 0], id="should return 2 dime"),
            pytest.param(
                40,
                [0, 1, 1, 1],
                id="should return 2 pennies + 1 nickel + 1 dime + 1 quarters",
            ),
        ],
    )
    def test_utmost_cases(self, cents: int, result: tuple) -> None:
        assert get_coin_combination(cents) == result
