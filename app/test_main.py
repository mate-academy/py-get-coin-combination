import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected",
        [
            (
                1,
                [1, 0, 0, 0]
            ),
            (
                5,
                [0, 1, 0, 0]
            ),
            (
                10,
                [0, 0, 1, 0]
            ),
            (
                25,
                [0, 0, 0, 1]
            )
        ]
    )
    def test_should_return_correct_coins_list(self,
                                              cents,
                                              expected):
        assert get_coin_combination(cents) == expected

    def test_should_return_list_of_integers(self):
        for coin in get_coin_combination(-2005):
            assert coin > 0
