import pytest

from app.main import get_coin_combination


class TestGetCoinCombinationClass:
    @pytest.mark.parametrize(
        "cents,expected_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="cents=0, res=[0,0,0,0]"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="cents=1, res=[1,0,0,0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="cents=6, res=[1,1,0,0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="cents=17, res=[2,1,1,0]"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="cents=50, res=[0,0,0,2]"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_list: list
    ) -> None:
        assert get_coin_combination(cents) == expected_list
