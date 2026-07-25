import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (11, [1, 0, 1, 0]),
        (30, [0, 1, 0, 1])
    ]
)
def test_coin(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_not_only_pennies() -> None:
    assert get_coin_combination(6) != [6, 0, 0, 0]


def test_uses_different_coins() -> None:
    result = get_coin_combination(41)
    assert result[-1] == 1
    assert result[1] == 1
    assert sum(result) < 41
