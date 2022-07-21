import pytest

from app.main import get_coin_combination


class TestOfTypeCombination:
    @pytest.mark.parametrize("initial_cents, expected",
                             [
                                 pytest.param(
                                     4,
                                     [4, 0, 0, 0],
                                     id="should return only penny "

                                 ),
                                 pytest.param(
                                     5,
                                     [0, 1, 0, 0],
                                     id="should return only nickel"
                                 ),
                                 pytest.param(
                                     10,
                                     [0, 0, 1, 0],
                                     id="should return only dime"
                                 ),
                                 pytest.param(
                                     25,
                                     [0, 0, 0, 1],
                                     id="should return only quarter "
                                 ),
                                 pytest.param(
                                     93,
                                     [3, 1, 1, 3],
                                     id="should return different types of coins"
                                 )
                             ]
                             )
    def test_modify_of_get_coin_combination(self, initial_cents, expected):
        assert get_coin_combination(initial_cents) == expected
