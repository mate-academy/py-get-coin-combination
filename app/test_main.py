import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (43, [3, 1, 1, 1]),
        (58, [3, 1, 0, 2]),
    ],
    ids=[
        "zero_cents",
        "one_cent",
        "five_cents",
        "ten_cents",
        "twenty_five_cents",
        "thirty_cents",
        "fifty_cents",
        "ninety_nine_cents",
        "one_hundred_cents",
        "forty_three_cents",
        "fifty_eight_cents",
    ]
)
def test_get_coin_combination(
        cents: int, expected: list[int, int, int, int]
) -> None:
    assert get_coin_combination(cents) == expected
