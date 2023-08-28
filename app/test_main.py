import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "coins,expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="1 coin should convert to 1 cent"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="6 coins should convert to 1 nickel and 1 cent"
            ),
            pytest.param(
                15,
                [0, 1, 1, 0],
                id="15 coins should convert to 1 dime and 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="17 coins should convert to 1 dime, 1 nickel and 2 cents"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="50 coins should convert to 2 quartets"
            ),
            pytest.param(
                111,
                [1, 0, 1, 4],
                id="111 coins should convert to 4 quarters, 1 dime and 1 cent"
            ),
            pytest.param(
                127,
                [2, 0, 0, 5],
                id="127 coins should convert to 5 quartets and 2 cents"
            ),
            pytest.param(
                199,
                [4, 0, 2, 7],
                id="111 coins should convert to 7 quarters 2 dimes and 4 cents"
            )
        ]
    )
    def test_cat_and_dog_years(self, coins: int,expected_result: list) -> None:
        assert get_coin_combination(coins) == expected_result
