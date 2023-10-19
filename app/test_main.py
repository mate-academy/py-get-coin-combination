import pytest

from app.main import get_coin_combination


# write your tests here1
@pytest.mark.parametrize(
    "cents, expected_output",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (4, [4, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (24, [4, 0, 2, 0]),
        (27, [2, 0, 0, 1]),
    ],
    ids=[
        "One penny",
        "One nickel",
        "One dime",
        "One quarter",
        "Close to one nickel",
        "One nickel and four pennies",
        "Two dimes and four pennies",
        "One quarter and 2 pennies",
    ]
)
def test_get_coin_combination(cents: int, expected_output: list) -> None:
    assert get_coin_combination(cents) == expected_output