from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1])
    ],
    ids=[
        "Zero cents return zero",
        "1 cent -> 1 penny",
        "6 cents -> 1 penny, 1 nickel",
        "17 cents -> two penny, 1 nickel, 1 dime",
        "50 cents -> 2 quarters",
        "41 cents -> 1 penny, 1 nickel, 1 dime, 1 quarter"
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
