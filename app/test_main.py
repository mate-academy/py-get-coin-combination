import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2])
])
def test_get_coin_combination_for_simple_value(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    (2, [2, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (9, [4, 1, 0, 0]),
    (11, [1, 0, 1, 0]),
    (14, [4, 0, 1, 0]),
    (16, [1, 1, 1, 0]),
    (24, [4, 0, 2, 0]),
    (26, [1, 0, 0, 1]),
])
def test_get_coin_combination_for_difficult_value(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    (41, [1, 1, 1, 1]),
    (66, [1, 1, 1, 2]),
    (46, [1, 0, 2, 1]),
    (42, [2, 1, 1, 1]),
    (82, [2, 1, 0, 3]),
    (111, [1, 0, 1, 4]),
    (222, [2, 0, 2, 8]),
    (333, [3, 1, 0, 13]),
    (444, [4, 1, 1, 17]),
    (555, [0, 1, 0, 22])
])
def test_get_coin_combination_for_mixed_values(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected
