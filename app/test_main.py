import pytest

from app.main import get_coin_combination


class TestCoins:
    @pytest.mark.parametrize(
        "input_cents,expected_coins",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test pennies"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="test nickels"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="test dimes"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="test quarters"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="test use lowest coins"
            )
        ]
    )
    def test_function(self,
                      input_cents: int,
                      expected_coins: list) -> None:
        assert get_coin_combination(input_cents) == expected_coins
