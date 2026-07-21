from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,coins", [
        pytest.param(
            0, [0, 0, 0, 0],
            id="when value equals to zero"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="small value"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="large amount"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="two quarters"
        ),
        pytest.param(
            99, [4, 0, 2, 3],
            id="maximum value"
        )
    ]
)
def test_coin_combination(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
