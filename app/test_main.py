from typing import Any
import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="list of 0 if cents is 0"
            ),
            pytest.param(
                57.91,
                [2.0, 1.0, 0.0, 2.0],
                id="correct result if cents is float"
            ),
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="if cents less than 5"
            ),
            pytest.param(
                7,
                [2, 1, 0, 0],
                id="if cents less than 10"
            ),
            pytest.param(
                21,
                [1, 0, 2, 0],
                id="if cents less than 25"
            ),
            pytest.param(
                44,
                [4, 1, 1, 1],
                id="if cents less than 50"
            ),
            pytest.param(
                108823,
                [3, 0, 2, 4352],
                id="if cents is very large"
            )
        ]
    )
    def test_for_different_cents(self, cents: int, coins_result: list) -> None:
        assert get_coin_combination(cents) == coins_result

    @pytest.mark.parametrize(
        "incorrect_cents, expected_error",
        [
            pytest.param(
                ("cents", {}, [], ()),
                TypeError,
                id="incorrect argument 'cents'"
            )
        ]
    )
    def test_for_incorrect_argument(
            self,
            incorrect_cents: Any,
            expected_error: TypeError
    ) -> None:
        for cents in incorrect_cents:
            with pytest.raises(expected_error):
                get_coin_combination(cents)
