from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (51, [1, 0, 0, 2])
    ],
    ids=[
        "1 penny",
        "1 penny and 1 nickel",
        "2 pennies, 1 nickel and 1 dime",
        "1 penny and 2 quarters"
    ]
)
def test_get_coin_combination(cents: int, expected_result: list[int]) -> None:
    assert get_coin_combination(cents) == expected_result
