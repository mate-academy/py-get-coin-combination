import pytest
from app.main import get_coin_combination


class TestCoins:
    @pytest.mark.parametrize(
        "value,result",

        [
            pytest.param(1, [1, 0, 0, 0],
                         id="return only cents"),
            pytest.param(5, [0, 1, 0, 0],
                         id="return only nickel"),
            pytest.param(10, [0, 0, 1, 0],
                         id="return only dimes"),
            pytest.param(25, [0, 0, 0, 1],
                         id="return only quarters"),
            pytest.param(68, [3, 1, 1, 2],
                         id="different types of coins"),

        ]
    )
    def test_coins(self, value: int, result: list) -> None:
        assert get_coin_combination(value) == result

    @pytest.mark.parametrize(
        "values,expected_error",

        [
            pytest.param(([2, 3], "coin", {}), TypeError,
                         id="test different types"),
        ]
    )
    def test_incorrect_input(self,
                             values: tuple,
                             expected_error: Exception) -> None:
        for value in values:
            with pytest.raises(TypeError):
                get_coin_combination(value)
