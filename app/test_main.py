import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "coins, expected_result",
        [
            pytest.param(
                1, [1, 0, 0, 0], id="should return 1 penny for 1 coin"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return 1 penny + 1 nickel for 6 coins",
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return 2 pennies + 1 nickel + 1 dime for 17 coins",
            ),
            pytest.param(
                50, [0, 0, 0, 2], id="should return 2 quarters for 50 coins"
            ),
        ],
    )

    def test_get_coin_combination(
            self,
            coins: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(coins) == expected_result
