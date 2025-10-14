import pytest
from app.main import get_coin_combination


def test_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies():
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_only_nickels():
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]  # Prefer 1 dime over 2 nickels


def test_only_dimes():
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_quarters():
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_mixed_coins():
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]  # ✅ Corrected to minimal coin count


def test_large_amount():
    assert get_coin_combination(1234) == [4, 1, 0, 49]


def test_all_coin_types_used():
    result = get_coin_combination(41)
    assert result == [1, 1, 1, 1], "Should use all coin types for 41 cents"


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),        # only pennies
        (6, [1, 1, 0, 0]),        # pennies + nickels
        (17, [2, 1, 1, 0]),       # pennies + nickels + dimes
        (50, [0, 0, 0, 2]),       # only quarters
        (99, [4, 0, 2, 3]),       # mix of all types
    ]
)
def test_get_coin_combination_variety(cents, expected) -> None:
    assert get_coin_combination(cents) == expected


def test_all_coin_types_used_param() -> None:
    result = get_coin_combination(99)
    assert result == [4, 0, 2, 3], "Should use multiple coin types for optimal combination"
    assert sum(result) == 9, "Should use minimal number of coins"
