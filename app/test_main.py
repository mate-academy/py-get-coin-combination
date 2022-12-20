import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result", [
            pytest.param(1, [1, 0, 0, 0],
                         id="should return 1 penny"),
            pytest.param(6, [1, 1, 0, 0],
                         id="should return 1 penny + 1 nickel"),
            pytest.param(17, [2, 1, 1, 0],
                         id="should return 2 penny + 1 nickel + 1 dime"),
            pytest.param(50, [0, 0, 0, 2],
                         id="should return 2 quarter"),
        ]
    )
    def test_coin_combination(self, cents, expected_result):
        assert get_coin_combination(cents) == expected_result
