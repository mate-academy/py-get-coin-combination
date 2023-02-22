from app.main import get_coin_combination
import pytest


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_res",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="value equal zero"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="cent`s value equal 1"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="value equal 6"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="value equal 17"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="value equal 50"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_res: list
    ) -> None:
        assert get_coin_combination(cents) == expected_res
