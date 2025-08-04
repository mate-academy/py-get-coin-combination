import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ],
    ids=[
        "should return list of 0 for 0 cents",
        "should return 1 penny for 1 cent",
        "should return 1 nickel for 5 cents",
        "should return 1 dime for 10 cents",
        "should return 1 quarter for 25 cents"
    ]
)
def test_get_coin_combination_single_coin(
        cents: int,
        expected: list[int]
) -> None:
    actual = get_coin_combination(cents)

    assert actual == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (6, [1, 1, 0, 0]),
        (15, [0, 1, 1, 0]),
        (35, [0, 0, 1, 1])
    ],
    ids=[
        "should return 1 penny and 1 nickel for 6 cents",
        "should return 1 nickel and 1 dime for 15 cents",
        "should return 1 dime 1 quarter for 35 cents"
    ]
)
def test_get_coin_combination_combination(
        cents: int,
        expected: list[int]
) -> None:
    actual = get_coin_combination(cents)

    assert actual == expected
