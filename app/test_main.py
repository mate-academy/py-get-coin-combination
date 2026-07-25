from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins, expected",
    [
        (7, [2, 1, 0, 0]),
        (0, [0, 0, 0, 0]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (88, [3, 0, 1, 3])
    ]
)
def test_coins(coins: int , expected: list) -> None:

    assert get_coin_combination(coins) == expected
