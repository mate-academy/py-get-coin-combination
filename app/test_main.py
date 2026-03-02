import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        (3, [3, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (7, [2, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (99, [4, 0, 2, 3])
    ], ids=[
        "should return only penny when given cents bellow 5",
        "should return only nickel when given cents equal to 5",
        "should return penny and nickel when given cents bellow 10",
        "should return dime when given cents equal to 10",
        "should return pennies, nickel, dime when given cents bellow 25",
        "should return quarters when given cents equal to 25",
        "should return proper number of coins of the same amount"
    ]
)
def test_should_return_proper_coin_combination(cents: int, expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins