import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
            "input,output",
            [
                pytest.param(
                    1,
                    [1, 0, 0, 0],
                    id="should return 1 penny for input 1"
                ),
                pytest.param(
                    6,
                    [1, 1, 0, 0],
                    id="should return 1 penny and 1 nickel for input 6"
                ),
                pytest.param(
                    17,
                    [2, 1, 1, 0],
                    id="should return 2p, 1n and 1n for input 17"
                ),
                pytest.param(
                    50,
                    [0, 0, 0, 2],
                    id="should return 2q, 1n and 1n for input 50"
                ),
            ]
    )
    def test_should_return_proper_output(self, input, output):
        assert get_coin_combination(input) == output