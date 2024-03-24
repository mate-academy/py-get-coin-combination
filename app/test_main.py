from app.main import get_coin_combination
import pytest


class TestConversionPennies:
    @pytest.mark.parametrize(
        "value_penny, expected_list",
        [
            pytest.param(
                2, [2, 0, 0, 0],
                id="one cent coins should be checked"),

            pytest.param(
                6, [1, 1, 0, 0],
                id="should check that  could "
                   "return coins of pennies, nickel"),

            pytest.param(
                17, [2, 1, 1, 0],
                id="should check that  could "
                   "return coins of pennies, nickel, dime"),

            pytest.param(
                67, [2, 1, 1, 2],
                id="should check that  could "
                   "return coins of pennies, nickel, dime, quarters"),
        ]
    )
    def test_conversion_penny(self, value_penny: int,
                              expected_list: list) -> None:
        assert get_coin_combination(value_penny) == expected_list
