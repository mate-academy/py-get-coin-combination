from app.main import get_coin_combination
import pytest
from typing import List


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),            # No coins needed
        (1, [1, 0, 0, 0]),            # 1 penny
        (5, [0, 1, 0, 0]),            # 1 nickel
        (10, [0, 0, 1, 0]),           # 1 dime
        (25, [0, 0, 0, 1]),           # 1 quarter
        (6, [1, 1, 0, 0]),            # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),           # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),           # 2 quarters
        (99, [4, 0, 2, 3]),           # mixed combo with minimal coins
        (100, [0, 0, 0, 4])           # exactly 4 quarters
    ]
)
def test_get_coin_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_cannot_return_only_pennies() -> None:
    """Test that ensures function doesn't just return all pennies"""
    # These tests will fail if the function only returns pennies
    # Must use nickel, not 5 pennies
    assert get_coin_combination(5) == [0, 1, 0, 0]
    # Must use dime, not 10 pennies
    assert get_coin_combination(10) == [0, 0, 1, 0]
    # Must use quarter, not 25 pennies
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_must_use_mixed_coins() -> None:
    """Test that ensures function uses multiple coin types when needed"""
    # These tests will fail if function only uses one coin type per result
    result = get_coin_combination(17)  # Should be [2, 1, 1, 0]
    expected_msg = ("17 cents must use mixed coins: pennies, nickels, "
                    "and dimes, got {}")
    assert result == [2, 1, 1, 0], expected_msg.format(result)

    result = get_coin_combination(41)  # Should be [1, 1, 1, 1]
    expected_msg = "41 cents must use all four coin types, got {}"
    assert result == [1, 1, 1, 1], expected_msg.format(result)
