from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (64, [4, 0, 1, 2]),
        (0, [0, 0, 0, 0]),
    ])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        "0",
        [10],
        {10}
    ])
def test_invalid_cents_input(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
