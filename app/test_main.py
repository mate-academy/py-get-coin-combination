import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_coins, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (75, [0, 0, 0, 3]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3])
    ]
)
def test_coins_combination(
    cents_coins: int,
    result: list
) -> None:
    assert get_coin_combination(cents_coins) == result
