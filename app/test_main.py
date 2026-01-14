import pytest
import app.main as main


# =============================================================================
# Basic examples from the specification
# =============================================================================

def test_one_cent() -> None:
    """1 cent should return 1 penny."""
    assert main.get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cents() -> None:
    """6 cents should use a penny and a nickel."""
    assert main.get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cents() -> None:
    """17 cents should combine pennies, a nickel and a dime."""
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty_cents() -> None:
    """50 cents should be represented by two quarters."""
    assert main.get_coin_combination(50) == [0, 0, 0, 2]


# =============================================================================
# Total value validation
# =============================================================================

@pytest.mark.parametrize("cents", [0, 4, 9, 14, 23, 41, 99])
def test_total_value_is_correct(cents: int) -> None:
    """Returned coins must sum up to the original value."""
    pennies, nickels, dimes, quarters = main.get_coin_combination(cents)

    total = (
        pennies
        + nickels * 5
        + dimes * 10
        + quarters * 25
    )

    assert total == cents


# =============================================================================
# Tests that prevent incorrect implementations
# =============================================================================

def test_uses_quarter_when_possible() -> None:
    """A quarter must be used when the value is at least 25."""
    _, _, _, quarters = main.get_coin_combination(25)
    assert quarters == 1


def test_uses_dime_and_nickel() -> None:
    """15 cents should use one dime and one nickel."""
    assert main.get_coin_combination(15) == [0, 1, 1, 0]


def test_uses_mixed_coins() -> None:
    """
    41 cents requires a mix of all coin types.
    This prevents single-coin-type implementations.
    """
    assert main.get_coin_combination(41) == [1, 1, 1, 1]


def test_not_only_pennies_for_large_values() -> None:
    """Large values must not be represented using only pennies."""
    pennies, nickels, dimes, quarters = main.get_coin_combination(30)
    assert nickels + dimes + quarters > 0
    assert pennies < 30


def test_not_single_coin_type() -> None:
    """More than one coin type must be used when possible."""
    result = main.get_coin_combination(30)
    non_zero_types = sum(1 for count in result if count > 0)
    assert non_zero_types > 1
