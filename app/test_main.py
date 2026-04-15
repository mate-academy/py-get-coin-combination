import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_returns_list() -> None:
    result = get_coin_combination(10)
    assert isinstance(result, list)


def test_get_coin_combination_length() -> None:
    result = get_coin_combination(10)
    assert len(result) == 4
