import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (2, [2, 0, 0, 0]),
        (12, [2, 0, 1, 0]),
        (37, [2, 0, 1, 1]),
    ]
)
def test_should_return_the_smallest_number_of_coins(
        cents: int,
        coins: list
) -> None:
    assert (
        get_coin_combination(cents) == coins
    )
