import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize("cents,expected", [
        pytest.param(1, [1, 0, 0, 0],
                     id="Should return 1 penny for 1 cent"),
        pytest.param(6, [1, 1, 0, 0],
                     id="Should return 1 nickel for 5 cents"),
        pytest.param(17, [2, 1, 1, 0],
                     id="Should return 1 dime for 10 cents"),
        pytest.param(50, [0, 0, 0, 2],
                     id="Should return 1 quarter for 25 cents")

    ])
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected
