import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Should return 1 penny if cents = 1."
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Should return 1 penny and 1 nickel if cents = 6."
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="Should return 2 penny, 1 nickel and 1 dime if cents = 17."
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="Should return 2 quarters if cents = 50."
            )
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            result: list
    ) -> None:
        assert get_coin_combination(cents) == result
