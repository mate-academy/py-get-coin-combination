import pytest
from typing import Type
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_list",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="should return zeros if cents are 0"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="should return the right amount of pennies"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="should return only a nickel"
            ),
            pytest.param(
                20, [0, 0, 2, 0],
                id="should return only dimes"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="should return only quarters"
            ),
            pytest.param(
                42, [2, 1, 1, 1],
                id="should return the right amount of each coin type"
            )

        ]
    )
    def test_should_return_list_with_right_amounts(
            self,
            cents: int,
            expected_list: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_list

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            ("17", TypeError)
        ]
    )
    def test_should_raise_error_with_wrong_data(
            self,
            cents: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
