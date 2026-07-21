import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_coins",
        [
            pytest.param(
                1, [1, 0, 0, 0],
                id="when input 1 cent the result should be [1, 0, 0, 0]"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="when input 6 cents the result should be [1, 1, 0, 0]"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="when input 17 cents the result should be [2, 1, 1, 0]"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="when input 50 cents the result should be [0, 0, 0, 2]"
            ),
            pytest.param(
                0, [0, 0, 0, 0],
                id="when input 0 cents the result should be [0, 0, 0, 0]"
            )
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  expected_coins: list) -> None:
        assert get_coin_combination(cents) == expected_coins
