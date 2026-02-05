import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    def test_coins_options_should_be_only_4(self) -> None:
        assert len(get_coin_combination(5)) == 4

    @pytest.mark.parametrize(
        "cents, expected_combination",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should have only pennies"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should have only pennies"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should have pennies and nickels"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should have pennies, nickels and dimes"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="should have pennies, nickels, dimes and quarters"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should have quarters only"
            ),
            pytest.param(
                35,
                [0, 0, 1, 1],
                id="should have dimes and quarters"
            ),
            pytest.param(
                40,
                [0, 1, 1, 1],
                id="should have nickels, dimes and quarters"
            ),

        ]
    )
    def test_correct_split_into_coins(
            self,
            cents: int,
            expected_combination: list
    ) -> None:
        assert get_coin_combination(cents) == expected_combination
