from typing import Any

import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ],
        ids=[
            "give 1 coin",
            "give 6 cons",
            "give 17 coins",
            "give 50 coins",
        ]
    )
    def test_getting_coins(
        self,
        cents: int,
        expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result


class TestExceptionsCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            ("1", TypeError),
        ],
    )
    def test_raising_error(
            self,
            cents: Any,
            expected_error: [TypeError]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
