import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),  # 1¢ → 1 penny
        (6, [1, 1, 0, 0]),  # 6¢ → 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),  # 17¢ → 2 pennies + 1 nickel + 1 dime
        (30, [0, 1, 0, 1]),  # 30¢ → 1 nickel + 1 quarter (minimal coins)
        (50, [0, 0, 0, 2]),  # 50¢ → 2 quarters
        (99, [4, 0, 2, 3]),  # 99¢ → 3 quarters + 2 dimes + 4 pennies
    ]
)
def test_get_coin_combination_param(cents: int, expected: list[int]) -> None:
    result = get_coin_combination(cents)
    assert result == expected, (
        f"Expected get_coin_combination({cents}) "
        f"to return {expected}, got {result}"
    )


def test_zero_cents_returns_no_coins() -> None:
    """0 cents should return [0, 0, 0, 0]."""
    assert get_coin_combination(0) == [0, 0, 0, 0]
