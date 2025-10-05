import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),          # no coins
        (1, [1, 0, 0, 0]),          # 1 penny
        (5, [0, 1, 0, 0]),          # 1 nickel
        (10, [0, 0, 1, 0]),         # 1 dime
        (25, [0, 0, 0, 1]),         # 1 quarter
        (6, [1, 1, 0, 0]),          # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),         # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),         # 2 quarters
        (41, [1, 1, 1, 1]),         # 1 penny + 1 nickel + 1 dime + 1 quarter
        (99, [4, 0, 2, 3]),         # optimal: 3 quarters + 2 dimes + 4 pennies
    ],
)
def test_get_coin_combination_examples_and_cases(
    cents: any,
    expected: any
) -> None:
    """Test provided examples and several edge cases."""
    assert get_coin_combination(cents) == expected


def test_large_amount_returns_minimal_number_of_coins() -> None:
    cents = 1000
    result = get_coin_combination(cents)
    # Check sum of coin values equals 1000
    total_value = result[0] + result[1] * 5 + result[2] * 10 + result[3] * 25
    assert total_value == cents
    # Ensure result is a list of four integers
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) and x >= 0 for x in result)
