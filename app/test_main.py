from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (1111, [1, 0, 1, 44]),
    ]
)
def test_get_coin_combination(cents: int, coins: int) -> None:
    assert get_coin_combination(cents) == coins


def test_get_coin_combination_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("not a number")
