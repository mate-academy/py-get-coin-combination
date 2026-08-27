import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (25, [0, 0, 0, 1]),
        (87, [2, 0, 1, 3]),
    ],
    ids=[
        "zero penny",
        "1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "1 off all type coints",
        "2 quarters",
        "1 quarters",
        "2 penny + 1 dime + 3 quaters",
    ],
)
def test_get_coin_combination(
        cents: int,
        expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected
