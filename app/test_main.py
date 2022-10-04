import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="Should return [0, 0, 0, 0] we have 0 cents"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="Should return [1, 0, 0, 0] we have 1 penny"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="Should return [1, 1, 0, 0] we have 1 penny + 1 nickel"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="Should return [2, 1, 1, 0] we have 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="Should return [0, 0, 0, 2] we have 2 quarters"
            ),
        ]
    )
    def test_coin_combination(self, cents: int, expected: int) -> None:
        assert get_coin_combination(cents) == expected
