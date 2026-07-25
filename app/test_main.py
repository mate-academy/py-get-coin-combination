import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="Should return zero coins for zero cents"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="Should return one penny for one cent"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="Should return one nickel for five cents"
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="Should return one dime for ten cents"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="Should return one quarter for twenty-five cents"
            ),
            pytest.param(
                41, [1, 1, 1, 1],
                id="Should return one of each coin for forty-one cents"
            ),
            pytest.param(
                99, [4, 0, 2, 3],
                id="More than one of each coin"
            ),
        ],
    )
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected
