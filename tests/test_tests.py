import pytest
from app.main import get_coin_combination  # Ensure correct import

@pytest.mark.parametrize("cents, expected_options", [
    (1, [[1, 0, 0, 0]]),   # Only pennies
    (5, [[0, 1, 0, 0]]),   # Only nickels
    (10, [[0, 0, 1, 0]]),  # Only dimes
    (25, [[0, 0, 0, 1]]),  # Only quarters
    (30, [[0, 0, 3, 0], [0, 1, 0, 1]]),  # 3 dimes OR 1 quarter + 1 nickel
    (99, [[4, 0, 2, 3]])   # Mixed case
])
def test_various_cases(cents, expected_options):
    """Ensure get_coin_combination handles various cases correctly."""
    assert get_coin_combination(cents) in expected_options, f"Unexpected result for {cents} cents"

def test_return_mixed_coins():
    """Ensure get_coin_combination returns different coin types when needed."""
    assert get_coin_combination(6) == [1, 1, 0, 0], "Should return both pennies and nickels"
    assert get_coin_combination(17) == [2, 1, 1, 0], "Should return pennies, a nickel, and a dime"
    assert get_coin_combination(99) == [4, 0, 2, 3], "Should return pennies, dimes, and quarters"

def test_not_only_pennies():
    """Ensure get_coin_combination does not return only pennies when larger denominations are possible."""
    result = get_coin_combination(10)  # Should be [0, 0, 1, 0] (1 dime)
    assert result[0] == 0, "Should not use pennies when dimes are available"

def test_not_only_one_type():
    """Ensure get_coin_combination does not return only one type when multiple types are needed."""
    result = get_coin_combination(27)  # Should be [2, 0, 0, 1] (2 pennies + 1 quarter)
    assert result.count(0) < 3, "Should return a mix of coin types"
