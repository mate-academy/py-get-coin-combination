import pytest

from typing import Any

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_cents,expected_coin_combiantion",
        [
            (
                1, [1, 0, 0, 0]
            ),
            (
                17, [2, 1, 1, 0]
            ),
            (
                50, [0, 0, 0, 2]
            ),
            (
                5, [0, 1, 0, 0]
            ),
            (
                1024, [4, 0, 2, 40]
            )
        ]
    )
    def test_right_coin_combinations(self,
                                     initial_cents: int,
                                     expected_coin_combiantion: list
                                     ) -> None:
        assert get_coin_combination(initial_cents
                                    ) == expected_coin_combiantion

    @pytest.mark.parametrize(
        "initial_cents,expected_error",
        [
            (
                "100", TypeError
            )
        ]
    )
    def test_right_error_raising(self,
                                 initial_cents: Any,
                                 expected_error: Any) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(initial_cents)
