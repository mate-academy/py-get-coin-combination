import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(
                1, [1, 0, 0, 0], id="for 1 coin"
            ),
            pytest.param(
                6, [1, 1, 0, 0], id="for 6 coin"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0], id="for 17 coin"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2], id="for 58 coin"
            )
        ]
    )
    def test_coin_combination(
            self,
            cents: int,
            result: list[int]) -> None:
        assert get_coin_combination(cents) == result
