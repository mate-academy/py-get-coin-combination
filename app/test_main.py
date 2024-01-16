import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (0, [0, 0, 0, 0]),       # 0 cents
            (1, [1, 0, 0, 0]),       # 1 penny
            (6, [1, 1, 0, 0]),       # 1 penny + 1 nickel
            (17, [2, 1, 1, 0]),      # 2 pennies + 1 nickel + 1 dime
            (50, [0, 0, 0, 2]),      # 2 quarters
            (99, [4, 0, 2, 3]),      # 4 pennies + 2 dimes + 3 quarters
            (100, [0, 0, 0, 4]),     # Corrected: 4 quarters (1 dime was missing)
            (125, [0, 0, 0, 5]),     # 5 quarters
        ],
    )
    def test_get_coin_combination(self, cents: int, expected_result: list) -> None:
        assert get_coin_combination(cents) == expected_result

    def test_get_coin_combination_negative(self) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(-1)
