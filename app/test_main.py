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
        (6, [1, 1, 0, 0]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (1000, [0, 0, 0, 40]),
        (8, [3, 1, 0, 0]),
        (14, [4, 0, 1, 0]),
        (65, [0, 1, 1, 2]),
        (73, [3, 0, 2, 2]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_negative() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-5)


def test_get_coin_combination_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("25")
