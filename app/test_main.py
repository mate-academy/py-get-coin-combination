import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, values",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ], ids=["penny", "penny_and_nickel", "penny_nickels_dime", "quarters"]
)
def test_get_coin_combination(coins: int, values: list) -> None:
    assert get_coin_combination(coins) == values
