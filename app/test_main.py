from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents_input,result_list",
        [
            pytest.param(
                41, [1, 1, 1, 1],
                id="Should fill all resulting list"
            ),
            pytest.param(
                40, [0, 1, 1, 1],
                id="Should fill all resulting list except penny"
            ),
            pytest.param(
                35, [0, 0, 1, 1],
                id="Should fill all resulting list except nickel"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="Should fill all resulting list except dime"
            ),
            pytest.param(
                0, [0, 0, 0, 0],
                id="Should return empty list"
            )
        ]
    )
    def test_get_coin_combination(self,
                                  cents_input: int,
                                  result_list: list[int]) -> None:
        assert get_coin_combination(cents_input) == result_list
