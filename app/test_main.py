import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination_basic(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_non_negative_only() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-5)


def test_increasing_amount_changes_output() -> None:
    result1 = get_coin_combination(24)
    result2 = get_coin_combination(25)
    assert result1 != result2
