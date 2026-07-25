import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_converted_cents",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return zeroes if cents equal 0"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should convert 1 cent to 1 penny"
            ),
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="should return only penny if cents less than 5"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="should convert 5 cents to 1 nickel"
            ),
            pytest.param(
                9,
                [4, 1, 0, 0],
                id="should return penny, nickel if cents less than 10"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="should convert 10 cent to 1 dime"
            ),
            pytest.param(
                16,
                [1, 1, 1, 0],
                id="should return penny, nickel, dime if cents less than 25"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="should convert 25 cent to 1 quarter"
            ),
            pytest.param(
                116,
                [1, 1, 1, 4],
                id="should accurately convert large cents"
            ),
            pytest.param(
                10000,
                [0, 0, 0, 400],
                id="should accurately convert extremely large cents"
            ),
            pytest.param(
                35.8,
                [0, 0, 1, 1],
                id="should accurately convert float cents"
            ),
        ]
    )
    def test_convert_cents_correctly_and_sum(
            self,
            cents: int | float,
            expected_converted_cents: list
    ) -> None:
        assert get_coin_combination(cents) == expected_converted_cents

    @pytest.mark.parametrize(
        "cents, expected_error",
        [
            pytest.param(
                "23",
                TypeError,
                id="should raise error for string cents"
            ),
            pytest.param(
                None,
                TypeError,
                id="should raise error for None types"
            ),
        ]
    )
    def test_get_coin_combination_exceptions(
            self,
            cents: str | None,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)

    def test_sum_of_coin_should_be_equal_to_cents(self) -> None:
        values = [1, 5, 10, 25]
        sum_of_coins = 0
        cents = 86
        coins = get_coin_combination(cents)

        for i in range(4):
            sum_of_coins += values[i] * coins[i]

        assert sum_of_coins == cents
