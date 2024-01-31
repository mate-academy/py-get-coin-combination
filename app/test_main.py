import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (57, [2, 1, 0, 2]),
    ],
    ids=[
        "should return zeros if given zero cents",
        "should be able to return pennies",
        "should be able to return pennies and other values (nickels)",
        "should be able to return only nickels",
        "should be able to return only dimes",
        "should be able to return only quarters",
        "should be able to return all types of money",
        "should be able to return list with values more than zero",
    ]
)
def test_get_coin_combination(
        cents: int,
        expected_result: list[int]
) -> None:
    result = get_coin_combination(cents)
    assert result == expected_result
