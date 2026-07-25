import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "initial_numbers_cent, expected_monet_list",
        [
            (
                pytest.param(
                    0,
                    [0, 0, 0, 0],
                    id="should convert zero cents value"
                )
            ),
            (
                pytest.param(
                    1,
                    [1, 0, 0, 0],
                    id="should convert one cents to one pennie"
                )
            ),
            (
                pytest.param(
                    6,
                    [1, 1, 0, 0],
                    id="should convert six cents "
                       "to one pennie and one nickel"
                )
            ),
            (
                pytest.param(
                    17,
                    [2, 1, 1, 0],
                    id="should convert 17 cents "
                       "to 2 pennie, one nickel, one dime"
                )
            ),
            (
                pytest.param(
                    50,
                    [0, 0, 0, 2],
                    id="should convert 50 cents to 2 quarters"
                )
            )
        ]
    )
    def test_convert_combine_cents(self,
                                   initial_numbers_cent: int,
                                   expected_monet_list: list) -> None:
        assert get_coin_combination(
            initial_numbers_cent
        ) == expected_monet_list
