import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coin, expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="checking zero values"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="checking calculation 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="checking calculation 1 penny + 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="checking calculation 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="checking calculation 2 quarters"
            ),
            pytest.param(
                1000000000,
                [0, 0, 0, 40000000],
                id="checking calculation 2 quarters"
            ),
        ]
    )
    def test_get_coin(self,
                      coin: int,
                      expected_result: list) -> None:
        assert get_coin_combination(coin) == expected_result
