import pytest as pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "only pennies",
        "pennies and nickels",
        "pennies, nickels, dimes",
        "exactly quarters"
    ]
)
def test_combined_properly(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
