from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("coins,  result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "test for cent",
        "test for nickels",
        "test for dime",
        "test for quarters",
    ]
)
def test_get_coin_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result
