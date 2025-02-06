import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (17, [2, 1, 1, 0])
    ],
    ids=[
        "1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "2 quarters"
    ])
def test_if_calculates_proper_amount_of_coins(
        value: int, result: list[int]) -> None:
    assert get_coin_combination(value) == result
