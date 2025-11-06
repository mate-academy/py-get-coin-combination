import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination_basic(cents: int, expected: list[int]) -> None:
    """Basic correctness check for known values."""
    assert get_coin_combination(cents) == expected


def test_structure_and_types() -> None:
    """Ensure the result is always a list of four integers."""
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)


def test_total_value_matches_input() -> None:
    """Ensure total coin value matches the input cents."""
    for amount in [0, 1, 6, 17, 26, 50, 99]:
        pennies, nickels, dimes, quarters = get_coin_combination(amount)
        total = pennies + 5 * nickels + 10 * dimes + 25 * quarters
        assert total == amount


@pytest.mark.parametrize("amount", [6, 17, 26, 37, 99])
def test_uses_multiple_coin_types(amount: int) -> None:
    """
    Ensure that function uses at least two types of coins
    for non-trivial amounts (>=5 cents).
    """
    result = get_coin_combination(amount)
    non_zero_types = sum(1 for c in result if c > 0)
    assert (
        non_zero_types > 1
    ), f"For {amount} cents, expected multiple coin types, got {result}"
