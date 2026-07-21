import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "should return 1 penny",
        "should return 1 penny + 1 nickel",
        "should return 2 pennies + 1 nickel + 1 dime",
        "should return 2 quarters"
    ]
)
def test_correct_return(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
