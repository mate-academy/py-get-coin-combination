import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "coins_input, expected_result",
        [
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="should contain only penny when coins < 5"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should contain penny and nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should contain penny, nickel and dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should contain only quarters"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should contain zeros when no coins given"
            )
        ]
    )
    def test_get_coin_combination(
        self,
        coins_input: int,
        expected_result: list[int]
    ) -> None:
        assert get_coin_combination(coins_input) == expected_result
