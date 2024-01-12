from app.main import get_coin_combination
import pytest


class TestGetCoin:
    @pytest.mark.parametrize(
        "cents_nomination,expected_output",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="check 0 cents == list with 0s"
            ),
            pytest.param(
                2,
                [2, 0, 0, 0],
                id="check cents split in pennies"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="check cents split in 1 type of coins"
            ),
            pytest.param(
                43,
                [3, 1, 1, 1],
                id="check cents split in all types of coins"
            ),
        ]
    )
    def test_get_coin_on_correct_answer(
            self,
            cents_nomination: int,
            expected_output: list
    ) -> None:
        assert get_coin_combination(cents_nomination) == expected_output
