import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return 0"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="should return 1 nickel"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="should return 1 dime"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="should return 1 quarter"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 1 penny + 1 nickel"
        ),
        pytest.param(
            15,
            [0, 1, 1, 0],
            id="should return 1 nickel + 1 dime"
        ),
        pytest.param(
            35,
            [0, 0, 1, 1],
            id="should return 1 dime + 1 quarter"
        ),
        pytest.param(
            26,
            [1, 0, 0, 1],
            id="should return 1 penny + 1 quarter"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            99,
            [4, 0, 2, 3],
            id="should return 4 pennies + 2 dimes + 3 quarters"
        ),
        pytest.param(
            40,
            [0, 1, 1, 1],
            id="should return 1 nickel + 1 dime + 1 quarter"
        ),
        pytest.param(
            31,
            [1, 1, 0, 1],
            id="should return 1 penny + 1 nickel + 1 quarter"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return 1 penny + 1 nickel + 1 dime + 1 quarter"
        )
    ]
)
def test_get_coins_combination_correctly(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
