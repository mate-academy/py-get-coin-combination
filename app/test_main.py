from app.main import get_coin_combination
import pytest


class Test:
    @pytest.mark.parametrize(
        "amount,coins",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Test only one coin 'penny'"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Test two coins 'penny' and 'nickel'"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="Test three coins and two 'penny'"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="test only 'quarter' when the value is divided by a coin"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="Test use all the coins"
            )
        ]
    )
    def test_for_coins(self, amount: int, coins: list) -> None:
        assert get_coin_combination(amount) == coins
