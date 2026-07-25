from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coins, result",
        [
            pytest.param(6, [1, 1, 0, 0],
                         id="6 pennies: 1 nickel, 1 penny"),
            pytest.param(1, [1, 0, 0, 0],
                         id="1 penny: 1 penny"),
            pytest.param(0, [0, 0, 0, 0],
                         id="0 pennies must make a list of zeros"),
        ]
    )
    def test_get_coin_combination(self, coins: int, result: list) -> None:
        assert get_coin_combination(coins) == result

    @pytest.mark.parametrize(
        "coins",
        [
            pytest.param("10", id="coins type str must make TypeError"),
        ],
    )
    def test_should_raise_error_if_coins_value_is_not_integer(self,
                                                              coins: int) \
            -> None:
        with pytest.raises(TypeError):
            get_coin_combination(coins)
