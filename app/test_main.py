import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (99, [4, 0, 2, 3]),
        (41, [1, 1, 1, 1])
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected


def test_not_only_pennies() -> None:
    assert get_coin_combination(6) != [6, 0, 0, 0]


def test_multiple_coin_types() -> None:
    result = get_coin_combination(17)
    assert sum(1 for c in result if c > 0) > 1
