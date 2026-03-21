import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "number_of_cents,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "should return one penny for one cent.",
        "should return one penny one nickel for 6 pennies",
        "should return 2 pennies 1 nickel 1 dime for 17 pennies",
        "should return 2 quarters for 50 pennies"
    ]
)
def test_coin_combination(
    number_of_cents: int,
    expected_result: list
) -> None:
    assert get_coin_combination(number_of_cents) == expected_result
