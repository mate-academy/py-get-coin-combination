from typing import Any

import pytest

from app.main import get_coin_combination


class TestCoinCombination:

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                "8",
                TypeError,
                id="Expect TypeError if not int param"
            )
        ]
    )
    def test_coins_combination_raise_exceptions(
            self,
            cents: Any,
            expected_error: type[TypeError | ValueError]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)

    @pytest.mark.parametrize(
        "cents,expectation_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="Check zero"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Check one"
            ),
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="Check boundary parameter 4"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="Check boundary parameter 5"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Check boundary parameter 6 (5 and 1)"
            ),
            pytest.param(
                9,
                [4, 1, 0, 0],
                id="Check boundary parameter 9 (for 10)"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="Check boundary parameter 10"
            ),
            pytest.param(
                14,
                [4, 0, 1, 0],
                id="Check boundary parameter 14 (for 15)"
            ),
            pytest.param(
                15,
                [0, 1, 1, 0],
                id="Check boundary parameter 15"
            ),
            pytest.param(
                19,
                [4, 1, 1, 0],
                id="Check boundary parameter 19 (for 20)"
            ),
            pytest.param(
                20,
                [0, 0, 2, 0],
                id="Check boundary parameter 20"
            ),
            pytest.param(
                24,
                [4, 0, 2, 0],
                id="Check boundary parameter 25"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="Check boundary parameter 25"
            ),
        ]
    )
    def test_modify_coins_combinations_correctly(
            self,
            cents: int,
            expectation_list: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expectation_list
