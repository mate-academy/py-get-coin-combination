from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero",
        "1 cent",
        "2 cents",
        "5 cents",
        "6 cents",
        "10 cents",
        "17 cents",
        "25 cents",
        "30 cents",
        "50 cents",
        "99 cents",
    ],
)
def test_get_coin_combination(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected
