import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "quantity, expected",
        [
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (0, [0, 0, 0, 0]),
            (41, [1, 1, 1, 1]),
            (1234, [4, 1, 0, 49])
        ],
        ids=[
            "Test 1 cent is equal to 1 penny",
            "Test 5 cent's is equal to 1 nickel",
            "Test 10 cent's is equal to 1 dime",
            "Test 25 cent's is equal to 1 quarter",
            "Test 0 cent's is equal to [0, 0, 0, 0]",
            "Test many cant's can be calculated at the same time",
            "Test of great value"
        ]
    )
    def test_get_coin_combination(self, quantity: int, expected: list) -> None:
        assert get_coin_combination(quantity) == expected
