import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    ("cents", "expected"),
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination_returns_expected_coin_counts(
    cents: int, expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_uses_the_largest_coins_first() -> None:
    assert get_coin_combination(30) == [0, 1, 0, 1]
