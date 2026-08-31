import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        # Zero cents (edge case)
        (0, [0, 0, 0, 0]),
        # Single coin types
        (1, [1, 0, 0, 0]),   # 1 penny
        (5, [0, 1, 0, 0]),   # 1 nickel
        (10, [0, 0, 1, 0]),  # 1 dime
        (25, [0, 0, 0, 1]),  # 1 quarter
        # Combinations of multiple coin types
        (6, [1, 1, 0, 0]),   # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),  # 2 quarters
        # Complex and larger amounts
        (41, [1, 1, 1, 1]),  # 1 penny + 1 nickel + 1 dime + 1 quarter
        (99, [4, 0, 2, 3]),  # 4 pennies + 2 dimes + 3 quarters
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
