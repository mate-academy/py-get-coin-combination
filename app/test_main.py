import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_cents, expected_result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (0, [0, 0, 0, 0]),
        ]
    )
    def test_get_coin_combination(
            self,
            initial_cents: int,
            expected_result: int
    ) -> None:
        assert expected_result == get_coin_combination(initial_cents)
