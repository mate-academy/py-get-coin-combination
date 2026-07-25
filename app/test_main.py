from typing import Type

import pytest

from app.main import get_coin_combination


class TestCoinCombinationClass:
    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should be list with [1,0,0,0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should be list with [1, 1, 0, 0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should be list with [2, 1, 1, 0]"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should be list with [0, 0, 0, 2]"
            )
        ]
    )
    def test_check_result(
            self,
            cents: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result


class TestExpectedError:
    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                "5",
                TypeError,
                id="should raise error if values ages is not int"
            )
        ]
    )
    def test_raising_correctly(
            self,
            cents: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
