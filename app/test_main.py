import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id=("when 1 cent")
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id=("when 5 cents")
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id=("when 6 cents")
        ),
        pytest.param(
            18,
            [3, 1, 1, 0],
            id=("when 18 cents")
        ),
        pytest.param(
            43,
            [3, 1, 1, 1],
            id=("when 43 cents")
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id=("when 50 cents")
        )
    ]
)
def test_of_get_coin_combination(cents: int, coins: list) -> None:
    assert (
        get_coin_combination(cents) == coins
    )
