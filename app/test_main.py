import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "1 penny",
        "6 penny",
        "17 penny",
        "50 penny",
    ]
)
def test_(coins: int, result: list) -> None:
    assert (
            get_coin_combination(coins) == result
    ), f" {coins} penny  should be equal to list {result}"