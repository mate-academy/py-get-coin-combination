import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents_amount,expected",
        [
            pytest.param(
                17, [2, 1, 1, 0],
                id="17 penny should return [2, 1, 1, 0].",
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="1 penny should return [1, 0, 0, 0].",
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="6 penny should return [1, 1, 0, 0].",
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="17 penny should return [2, 1, 1, 0].",
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="50 penny should return [0, 0, 0, 2].",
            ),
        ]
    )
    def test_get_coin_combination(
            self,
            cents_amount: int,
            expected: list[int]
    ) -> None:
        assert get_coin_combination(cents_amount) == expected
