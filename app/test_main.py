import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, values",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (26, [1, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(coins: int, values: list) -> None:
    assert get_coin_combination(coins) == values
