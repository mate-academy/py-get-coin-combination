from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (41, [1, 1, 1, 1]),
        (24, [4, 0, 2, 0]),
        (26, [1, 0, 0, 1]),
    ],
)
def test_coin(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins


@pytest.mark.parametrize("cents", ["15", None])
def test_coin_tupe(cents : None | str) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
