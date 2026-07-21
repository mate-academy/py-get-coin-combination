from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(5, [0, 1, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(10, [0, 0, 1, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2]),
    ]
)
def test_cents(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
