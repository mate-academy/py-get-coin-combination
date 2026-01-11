from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_list",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "both_zero",
            "cent_into_pennie",
            "cent_into_pennie_and_nickel",
            "cent_into_2pennies_and_nickel_and_dime",
            "cent_into_2quarters"
        ]
    )
    def test_get_coin_combination(self, cents: int,
                                  expected_list: list) -> None:
        assert get_coin_combination(cents) == expected_list
