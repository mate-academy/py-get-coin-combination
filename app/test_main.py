import pytest
from app import main  # from app.main import get_coin_combination


class TestCountAmountOfCoins:

    @pytest.mark.parametrize(
        "amount_of_cents,expected_combination",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (9, [4, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (11, [1, 0, 1, 0]),
            (24, [4, 0, 2, 0]),
            (25, [0, 0, 0, 1]),
            (26, [1, 0, 0, 1])
        ],
    )
    def test_counts_amount_of_coin_correctly(
        self,
        amount_of_cents: int,
        expected_combination: list[int]
    ) -> None:
        assert main.get_coin_combination(amount_of_cents) == expected_combination


    @pytest.mark.parametrize(
        "amount_of_cents",
        [
            (-1),
            (-5)
        ],
    )
    def test_raises_value_error_for_negative_amount(
        self,
        amount_of_cents: int
    ) -> None:
        with pytest.raises(ValueError):
            main.get_coin_combination(amount_of_cents)


    @pytest.mark.parametrize(
        "amount_of_cents",
        [
            ("-1"),
            ("f")
        ],
    )
    def test_raises_type_error_for_non_int_amount(
        self,
        amount_of_cents: int
    ) -> None:
        with pytest.raises(TypeError):
            main.get_coin_combination(amount_of_cents)