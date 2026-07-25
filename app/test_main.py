import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (18, [3, 1, 1, 0]),
        (52, [2, 0, 0, 2]),
        (96, [1, 0 , 2, 3]),
        (0, [0, 0, 0, 0])
    ]
)
def test_get_coin_combination(coins: list, expected: list) -> None:
    assert get_coin_combination(coins) == expected
