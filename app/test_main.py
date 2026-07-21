import pytest
from app.main import get_coin_combination


def test_one_penny() -> None:
    """Test 1 cent returns one penny."""
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel_and_penny() -> None:
    """Test 6 cents gives 1 penny and 1 nickel."""
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_dime_nickel_and_pennies() -> None:
    """Test 17 cents gives 2 pennies, 1 nickel, and 1 dime."""
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    """Test 50 cents gives 2 quarters."""
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents() -> None:
    """Test 0 cents returns no coins."""
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_quarter() -> None:
    """Test 25 cents gives one quarter."""
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_complex_combination() -> None:
    """Test 99 cents gives correct minimal combination."""
    # 3 quarters (75) + 2 dimes (20) + 0 nickels + 4 pennies = 99
    assert get_coin_combination(99) == [4, 0, 2, 3]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (30, [0, 1, 0, 1]),  # 1 quarter + 1 nickel
        (41, [1, 1, 1, 1]),  # 1 of each type
        (99, [4, 0, 2, 3]),
    ],
)
def test_parametrized_cases(cents: int, expected: list[int]) -> None:
    """Test multiple coin combinations with parameterization."""
    assert get_coin_combination(cents) == expected
