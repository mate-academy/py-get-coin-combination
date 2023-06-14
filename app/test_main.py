import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,coins_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="When 0 coins are given, returns 0!"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="When 1 coin is given, returns 1 penny!"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="When 5 coins are given, returns 1 nickel!"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="When 10 coins are given, returns 1 dime!"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="When 0 coins are given, returns 1 quarter!"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="When 41 coins are given, "
                   "returns 1 coin of each denomination!"
            )
        ]
    )
    def test_get_coin_combination_results(
            self,
            cents: int,
            coins_list: list[int]) -> None:
        assert get_coin_combination(cents) == coins_list
