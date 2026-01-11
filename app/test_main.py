import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="func should return list of zeros if cents = 0"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="func should return 1 penny if cents = 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="func should return 1 penny and 1 nickel if cents = 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="func should return 2 penny, 1 nickel, 1 dime if cents = 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="func should return 2 dime if cents = 50"
        ),
    ]
)
def test_get_coin_combination_values(
        cents: int,
        coins: list[int]
) -> None:
    assert get_coin_combination(cents) == coins
