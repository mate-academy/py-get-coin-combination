import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result", [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_result
