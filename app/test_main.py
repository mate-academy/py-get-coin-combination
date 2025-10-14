import pytest
from app.main import get_coin_combination


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


def test_all_coin_types_used() -> None:
    result = get_coin_combination(99)
    assert result == [4, 0, 2, 3], "Should use multiple coin types for optimal combination"
    assert sum(result) == 9, "Should use minimal number of coins"
