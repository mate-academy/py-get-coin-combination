import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (19, [4, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (41, [1, 1, 1, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (51, [1, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (1_000_000, [0, 0, 0, 40_000]),
        (1_000_041, [1, 1, 1, 40_001]),
    ],
)
def test_get_coin_combination(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [-1, -5, -25, -100, -1_000_000],
)
def test_get_coin_combination_negative_values(
    cents: int,
) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    ["25", 25.0, 25.5, None, [], {}, (25,)],
)
def test_get_coin_combination_invalid_types(
    cents: object,
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
