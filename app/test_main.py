import pytest

from app.main import get_coin_combination


class TestResultGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="if 'cents' == 0 return '[0, 0, 0, 0]'"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return 1 penny + 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return 2 quarters"
            )
        ]
    )
    def test_get_min_coin_combination(
            self,
            cents: int,
            result: list[int]
    ) -> None:
        assert get_coin_combination(cents) == result
