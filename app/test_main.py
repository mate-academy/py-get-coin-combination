import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (42, [2, 1, 1, 1])
    ],
    ids=[
        "Zero cents returns list of zeros",
        "1 cent adds one pennie",
        "5 cents add one nickel",
        "10 cents add one dime",
        "25 cents add one quarter",
        "All cents should be converted"
    ]
)
def test_get_coin_combination(
        cents: int,
        result: list[int]
) -> None:
    assert get_coin_combination(cents) == result
