import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_amount,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1])
    ],
    ids=[
        "0 cents test",
        "return pennies",
        "return nickels",
        "return dimes",
        "return quarters",
        "return each coin"
    ]
)
def test_calculate_coins(cents_amount: int, result: list) -> None:
    assert get_coin_combination(cents_amount) == result
