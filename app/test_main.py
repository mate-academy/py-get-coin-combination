from app.main import get_coin_combination

import pytest


class TestCoinCombination:
    @pytest.mark.parametrize(
        "value,expected_result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (0, [0, 0, 0, 0]),
            (116, [1, 1, 1, 4])
        ]
    )
    def test_combination(
            self,
            value: int,
            expected_result: list,
    ) -> None:
        assert get_coin_combination(value) == expected_result
