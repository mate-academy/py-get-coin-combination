import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (51, [1, 0, 0, 2]),
        (1234, [4, 1, 0, 49]),
    ],
    ids=[
        "When we have only 1 pennie",
        "When we have penny and dime",
        "When we have pennies, nickel and dime",
        "When we have quarters and pennies",
        "When we have a large value"
    ]
)
def test_coin_combination(coin: int, result: list) -> None:
    assert get_coin_combination(coin) == result
