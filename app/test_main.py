import pytest

from app.main import get_coin_combination


def test_zero_cents_returns_no_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
    ],
)
def test_exact_coin_value_returns_one_coin(
    cents: int,
    expected: list,
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        (4, [4, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (26, [1, 0, 0, 1]),
    ],
)
def test_amounts_around_coin_values(
    cents: int,
    expected: list,
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (41, [1, 1, 1, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (123, [3, 0, 2, 4]),
    ],
)
def test_combination_uses_minimum_number_of_coins(
    cents: int,
    expected: list,
) -> None:
    assert get_coin_combination(cents) == expected
