from app.main import get_coin_combination
import pytest


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="Test function pennies combination"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Test function nickels and pennies combinations"
            ),
            pytest.param(
                16,
                [1, 1, 1, 0],
                id="Test function nickels, pennies, dimes combinations"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="Test function for all combinations"
            ),
        ]
    )
    def test_coin_combination(
            self,
            cents: int,
            result: list[int],
    ) -> None:
        assert get_coin_combination(cents) == result

    @pytest.mark.parametrize(
        "cents, error",
        [
            pytest.param(
                "1",
                TypeError,
                id="Value cents should be int, not str!"
            ),
            pytest.param(
                [1],
                TypeError,
                id="Value cents should be int, not list!"
            ),
            pytest.param(
                {1},
                TypeError,
                id="Value cents should be int, not dict!"
            ),
        ]
    )
    def test_coin_combination_value(
            self,
            cents: int,
            error: TypeError
    ) -> None:
        with pytest.raises(error):
            get_coin_combination(cents)
