import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "number,list_of_coins",
        [
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (7, [2, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (17, [2, 1, 1, 0]),
            (25, [0, 0, 0, 1]),
            (41, [1, 1, 1, 1])
        ]
    )
    def test_check_if_counted_coins_is_correct(
            self,
            number: int,
            list_of_coins: list
    ) -> None:
        assert get_coin_combination(number) == list_of_coins
