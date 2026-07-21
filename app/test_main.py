import pytest
from app.main import get_coin_combination  # adjust import if needed


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),      # 1 penny
        (5, [0, 1, 0, 0]),      # 1 nickel
        (6, [1, 1, 0, 0]),      # 1 penny + 1 nickel
        (10, [0, 0, 1, 0]),     # 1 dime
        (17, [2, 1, 1, 0]),     # 2 pennies + 1 nickel + 1 dime
        (25, [0, 0, 0, 1]),     # 1 quarter
        (50, [0, 0, 0, 2]),     # 2 quarters
        (99, [4, 0, 2, 3]),     # 3 quarters, 2 dimes, 0 nickels, 4 pennies
        (41, [1, 1, 1, 1]),     # 1 quarter, 1 dime, 1 nickel, 1 penny
    ]
)
def test_get_coin_combination_valid(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
