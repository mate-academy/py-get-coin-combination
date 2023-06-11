from app.main import get_coin_combination
import pytest


class TestCoinCombination:

    @pytest.mark.parametrize(
        "cents,result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (169, [4, 1, 1, 6]),
        ]
    )
    def test_coin_combination_is_correct(
            self,
            cents: int,
            result: list
    ) -> None:

        assert get_coin_combination(cents) == result

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                -15, ValueError,
                id="should raise error taking negative integer"
            ),
            pytest.param(
                "two", TypeError,
                id="should raise error taking string"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            cents: int,
            expected_error: type[Exception]
    ) -> None:

        with pytest.raises(expected_error):
            get_coin_combination(cents)
