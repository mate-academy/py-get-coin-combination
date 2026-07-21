import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
    ],
    ids=[
        "zero cents should return 0 coins",
        "1 cent should return 1 penny",
        "6 cents should return 1 penny, 1 nickel",
        "17 cents should return 2 penny, 1 nickel and 1 dime",
        "50 cents should return 2 quarters",
        "41 cents should return [penny, nickel, dime, quarter]"
    ]
)
def test_correct_combination(
        cents: int,
        coins: list[int]
) -> None:
    assert get_coin_combination(cents) == coins
