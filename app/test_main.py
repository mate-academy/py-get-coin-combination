from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "value, answer",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="test value = 0"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="test add 1 penny"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="test add 1 nickel "
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="test add 1 dime"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id=("test add 1 quarters")
            ),
        ]
    )
    def test_get_coin(self, value, answer):
        assert get_coin_combination(value) == answer
