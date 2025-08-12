import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize("cents, expected_coins", [
        pytest.param(
            0, [0, 0, 0, 0],
            id="no coins"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="1 cent = 1 penny"
        ),
        pytest.param(
            4, [4, 0, 0, 0],
            id="4 pennies"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="1 nickel"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="1 penny + 1 nickel"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="1 dime"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            23, [3, 0, 2, 0],
            id="3 pennies + 2 dimes"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="1 quarter"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="2 quarters"
        ),
        pytest.param(
            99, [4, 0, 2, 3],
            id="4 pennies + 2 dimes + 3 quarters"
        ),
    ])
    def test_get_coin_combination(
            self,
            cents: int,
            expected_coins: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_coins
