from app.main import get_coin_combination
import pytest


class TestCoins:

    @pytest.mark.parametrize(
        "amount, expected_result",
        (
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        )
    )
    def test_should_return_correct_values(
        self,
        amount: int,
        expected_result: list
    ) -> None:
        assert get_coin_combination(amount) == expected_result

    @pytest.mark.parametrize(
        "amount, expected_error",
        (
            ("error", TypeError),
        )
    )
    def test_should_rise_errors(
        self,
        amount: str,
        expected_error: type
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(amount)