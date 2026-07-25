import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (26, [1, 0, 0, 1]),
        (15, [0, 1, 1, 0]),
        (35, [0, 0, 1, 1]),
        (40, [0, 1, 1, 1]),
        (41, [1, 1, 1, 1]),
        (67, [2, 1, 1, 2]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],)
def test_coins_check_combination(coins: int, combination: list) -> None:
    assert get_coin_combination(coins) == combination
