import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (15, [0, 1, 1, 0]),
            (16, [1, 1, 1, 0]),
            (20, [0, 0, 2, 0]),
            (25, [0, 0, 0, 1]),
            (30, [0, 1, 0, 1]),
            (35, [0, 0, 1, 1]),
            (40, [0, 1, 1, 1]),
            (41, [1, 1, 1, 1]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_get_coin_combination(
        self,
        cents: int,
        expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result
