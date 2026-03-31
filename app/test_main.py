import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),   # 1 penny
        (6, [1, 1, 0, 0]),    # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),   # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),   # 2 quarters
        (99, [4, 0, 2, 3]),   # 4 pennies + 2 dimes + 3 quarters
        (0, [0, 0, 0, 0])   # no coins for 0 cents
    ]
)
def test_get_coin_combination(cents: int, expected: bool) -> None:
    result = get_coin_combination(cents)
    assert result == expected, f"Failed for {cents} cents: {result}"
