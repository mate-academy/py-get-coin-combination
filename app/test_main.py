import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (43, [3, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(
        cents: int,
        expected: list[int, int, int, int]
) -> None:
    get_coin_combination(cents)
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "invalid_cents",
    [-1, -2, -3, -10, -100, -9999]
)
def test_raises_error_for_negative_numbers(invalid_cents: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(invalid_cents)
