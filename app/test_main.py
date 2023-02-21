import pytest

from app.main import get_coin_combination


class TestGetCoinCombinationClass:
    @pytest.mark.parametrize(
        "get_coins, sorted_coins",
        [
            pytest.param(0, [0, 0, 0, 0],
                         id="must return 0"),
            pytest.param(1, [1, 0, 0, 0],
                         id="must return 1 penny"),
            pytest.param(6, [1, 1, 0, 0],
                         id="must return 1 penny + 1 nickel"),
            pytest.param(17, [2, 1, 1, 0],
                         id="must return 2 pennies + 1 nickel + 1 dime"),
            pytest.param(41, [1, 1, 1, 1],
                         id="must return 1 pennies + "
                            "1 nickel + 1 dime + quarter"),
            pytest.param(50, [0, 0, 0, 2],
                         id="must return 2 quarters")
        ]
    )
    def test_to_coin_combination(
            self,
            get_coins: int,
            sorted_coins: list
    ) -> None:
        assert get_coin_combination(get_coins) == sorted_coins
