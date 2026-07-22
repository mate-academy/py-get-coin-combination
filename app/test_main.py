import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (51, [1, 0, 0, 2]),
        (45, [0, 0, 2, 1]),
        (24, [4, 0, 2, 0]),
        (30, [0, 1, 0, 1])
    ],
    ids=[
        "1 cent = 1 penny",
        "5 cents = 1 nickel",
        "10 cents = 1 dime",
        "25 cents = 1 quarter",
        "41 cents = every coin by 1",
        "51 cents = 1 penny, 2 quarters",
        "45 cents = 2 dimes, 1 quarter",
        "24 cents = 4 pennies, 2 dimes",
        "30 cents = 1 nickel, 1 quarter"
    ]
)
def test_get_correct_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
