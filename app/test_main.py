import pytest
from app.main import get_coin_combination


class TestCoinCombinationClass:
    @pytest.mark.parametrize(
        "cents,result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="When coin amount equals to zero"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Penny and nickel test"
            ),
            pytest.param(
                60,
                [0, 0, 1, 2],
                id="Dime and quarters test"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="All kind of coins test"
            ),
            pytest.param(
                384,
                [4, 1, 0, 15],
                id="Large number test"
            )
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  result: list) -> None:
        assert get_coin_combination(cents) == result
