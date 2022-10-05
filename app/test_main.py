import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, amount_coins",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="test should return [0, 0, 0, 0] when amount of cents == 0"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="test should return [1, 0, 0, 0] when amount of cents == 1"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="test should return [0, 0, 0, 1] when amount of cents == 5"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="test should return [1, 1, 0, 0] when amount of cents == 6"
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="test should return [0, 0, 1, 0] when amount of cents == 10"
            ),
            pytest.param(
                11, [1, 0, 1, 0],
                id="test should return [1, 0, 1, 0] when amount of cents == 11"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="test should return [2, 1, 1, 0] when amount of cents == 17"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="test should return [0, 0, 0, 1] when amount of cents == 25"
            ),
            pytest.param(
                35, [0, 0, 1, 1],
                id="test should return [0, 0, 1, 1] when amount of cents == 35"
            ),
            pytest.param(
                40, [0, 1, 1, 1],
                id="test should return [0, 1, 1, 1] when amount of cents == 40"
            ),
            pytest.param(
                41, [1, 1, 1, 1],
                id="test should return [1, 1, 1, 1] when amount of cents == 41"
            ),
            pytest.param(
                67, [2, 1, 1, 2],
                id="test should return [2, 1, 1, 2] when amount of cents == 67"
            )
        ]
    )
    def test_should_return_possible_combination_coins(self, cents,
                                                      amount_coins):
        assert get_coin_combination(cents) == amount_coins
