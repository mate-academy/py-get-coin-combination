import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (106, [1, 1, 0, 4]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        "17",
        17.5,
        None,
        -1,
        -10,
    ]
)
def test_coins_raises_exception_on_invalid_types(cents: int) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_coin_combination(cents)
