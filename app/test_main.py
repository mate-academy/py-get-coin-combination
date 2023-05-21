import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_number, result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (42, [2, 1, 1, 1])
    ],
    ids=[
        "check the smallest positive integer",
        "check boundary amount",
        "check when cents combain of 2 coins",
        "check when cents combain 1 dime",
        "check combitation of 3 diffrent coins",
        "check when cents combain 1 quarter",
        "check when all coins used"
    ]
)
def test_combination_of_coins(cents_number: int, result: list) -> None:
    assert get_coin_combination(cents_number) == result
