import pytest
from app.main import get_coin_combination


class TestCoins:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (0, [0, 0, 0, 0]),  # Test zero cents
            (1, [1, 0, 0, 0]),  # Test one penny
            (5, [0, 1, 0, 0]),  # Test one nickel
            (10, [0, 0, 1, 0]),  # Test one dime
            (25, [0, 0, 0, 1]),  # Test one quarter
            (41, [1, 1, 1, 1]),  # Test mixed coins
            (99, [4, 0, 2, 3]),  # Test large value
            (68, [3, 1, 1, 2])
        ]
    )
    def test_get_coins(self, cents: int, expected_result: list) -> None:
        assert get_coin_combination(cents) == expected_result
