import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,coin_combination",
        [
            pytest.param(
                2, [2, 0, 0, 0],
                id="test 2 penny"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="test 1 penny + 1 nickel"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="test 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                66, [1, 1, 1, 2],
                id="test 1 penny + 1 nickel + 1 dime + 2 quarters"
            )
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  coin_combination: list) -> None:
        assert get_coin_combination(cents) == coin_combination
