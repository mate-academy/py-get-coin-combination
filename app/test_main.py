from pytest import mark

from app.main import get_coin_combination


class TestGetCoinCombination:
    @mark.parametrize(
        "cents, expected_coins_list",
        [
            (41, [1, 1, 1, 1]),
        ]
    )
    def test_should_return_different_coins(
            self,
            cents: int,
            expected_coins_list: list
    ) -> None:
        assert get_coin_combination(cents) == expected_coins_list
