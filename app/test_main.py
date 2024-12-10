import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),  # 1 penny
        (5, [0, 1, 0, 0]),  # 1 nickel
        (10, [0, 0, 1, 0]),  # 1 dime
        (25, [0, 0, 0, 1]),  # 1 quarter
        (50, [0, 0, 0, 2]),  # 2 quarters
    ],
)
def test_return_only_one_type(cents: int, expected: int) -> None:
    """
    Test cases where only one type of coin is needed.
    """
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
        (99, [4, 0, 2, 3]),  # 4 pennies + 2 dimes + 3 quarters
    ],
)
def test_return_multiple_types_of_coins(cents: int, expected: int) -> None:
    """
    Test cases where a combination of coin types is returned.
    """
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),  # No coins for 0 cents
    ],
)
def test_return_no_coins_for_zero_or_negative(
    cents: int, expected: int
) -> None:
    """
    Test edge cases where no coins should be returned.
    """
    assert get_coin_combination(cents) == expected
