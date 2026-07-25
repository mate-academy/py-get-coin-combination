import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected",
        [
            (
                41,
                [1, 1, 1, 1]
            ),
            (
                0,
                [0, 0, 0, 0]
            )
        ]
    )
    def test_should_return_correct_coins_list(self,
                                              cents,
                                              expected):
        assert get_coin_combination(cents) == expected
