import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination_returns_minimum_coins(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


def test_returns_list_of_length_four() -> None:
    result = get_coin_combination(42)
    assert isinstance(result, list)
    assert len(result) == 4
