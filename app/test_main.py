import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,min_coins_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="0 returns 0,0,0,0"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="1 penny returns 1,0,0,0"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="6 coins return 1,1,0,0"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="17 coins return 2,1,1,0"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="50 coins return 0,0,0,2"
            ),
            pytest.param(
                99,
                [4, 0, 2, 3],
                id="99 coins return 4,0,2,3"
            ),
            pytest.param(
                100,
                [0, 0, 0, 4],
                id="99 coins return 0,0,0,4"
            ),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            min_coins_list: list[int]
    ) -> None:
        assert get_coin_combination(cents) == min_coins_list
