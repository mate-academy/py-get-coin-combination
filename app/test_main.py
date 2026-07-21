import pytest

from app.main import get_coin_combination


class TestCentsToCoins:
    @pytest.mark.parametrize(
        "cents,expected_coins",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (68, [3, 1, 1, 2]),
        ]
    )
    def test_amount_of_cents_should_be_converted_to_correct_number_of_coins(
            self,
            cents: int,
            expected_coins: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_coins

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            ("8", TypeError),
            ([5], TypeError),
            ({35}, TypeError)
        ]
    )
    def test_should_raise_error_if_type_of_value_is_not_integer(
            self,
            cents: int,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
