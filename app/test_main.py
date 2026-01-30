import pytest
from app.main import get_coin_combination


class TestCoin:
    @pytest.mark.parametrize(
        "initial_cents,expected_result",
        [
            (17, [2, 1, 1, 0]),
            (25, [0, 0, 0, 1]),
            (0, [0, 0, 0, 0])
        ],
        ids=[
            "for 17 cents",
            "for 25 cents",
            "for 0 cents"
        ]
    )
    def test_should_return_correctly_numbers_of_cents(
            self,
            initial_cents: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(initial_cents) == expected_result

    @pytest.mark.parametrize(
        "initial_cents,expected_error",
        [
            ("apple", TypeError),
            ("", TypeError)
        ],
        ids=[
            "The variable 'cents' must be an integer!",
            "The 'cents' cannot be an empty string!"
        ]
    )
    def test_should_raise_an_error(
            self,
            initial_cents: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(initial_cents)
