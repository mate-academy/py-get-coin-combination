import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (116, [1, 1, 1, 4])
    ],
    ids=[
        "return list with 0 if no cents",
        "return 1 penny when cents = 1",
        "can correctly return nickel",
        "can correctly return dime",
        "can correctly return quarter",
        "return the smallest number of coins"
    ]
)
def test_could_return_different_combination_of_coins(
        cents: int,
        combination: list
) -> None:
    assert get_coin_combination(cents) == combination
