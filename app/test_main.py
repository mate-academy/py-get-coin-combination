import pytest

from app.main import get_coin_combination


cases = [
    (-10, [0, 0, 0, 0]),
    (-1, [0, 0, 0, 0]),
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (2, [2, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (15, [0, 1, 1, 0]),
    (35, [0, 0, 1, 1]),
    (40, [0, 1, 1, 1]),
    (41, [1, 1, 1, 1]),
    (100, [0, 0, 0, 4]),
    (153, [3, 0, 0, 6]),
    (116, [1, 1, 1, 4]),
    (74, [4, 0, 2, 2])
]


@pytest.mark.parametrize(
    "cents,coins",
    cases,
    ids=[f"{c} cents -> {coins}" for c, coins in cases]
)
def test_get_coin_combination_returns_correct_result(
        cents: int,
        coins: list[int]
) -> None:
    assert get_coin_combination(cents) == coins


def test_get_coin_combination_raises_error_when_not_valid_cents() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("12")
