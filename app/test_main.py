from __future__ import annotations
import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "test 0 cents",
        "test 1 cent",
        "test 6 cents",
        "test 17 cents",
        "test 50 cents"
    ]
)
def test_get_correct_coin_combination(
        cents: int,
        combination: list[int]
) -> None:
    assert get_coin_combination(cents) == combination
