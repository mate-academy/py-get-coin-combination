import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),        # 0 centów
        (1, [1, 0, 0, 0]),        # 1 penny
        (5, [0, 1, 0, 0]),        # 1 nickel
        (10, [0, 0, 1, 0]),       # 1 dime
        (25, [0, 0, 0, 1]),       # 1 quarter
        (6, [1, 1, 0, 0]),        # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),       # 2 pennies + 1 nickel + 1 dime
        (30, [0, 1, 0, 1]),       # 1 nickel + 1 quarter
        (41, [1, 1, 1, 1]),       # 1 of each coin
        (99, [4, 0, 2, 3]),       # 3 quarters + 2 dimes + 4 pennies
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    """Test various coin combinations for correctness."""
    assert get_coin_combination(cents) == expected
