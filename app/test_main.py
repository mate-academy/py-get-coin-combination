from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return 1 penny when cents is 1",
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return 1 penny + 1 nickel when cents is 6"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return 2 pennies + "
                   "1 nickel + 1 dime when cents is 17"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return should return 1 penny + 1 nickel "
                   "when cents is 6 when cents is 50"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return empty list when cents is 0"
            )
        ]
    )
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected
