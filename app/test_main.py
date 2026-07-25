import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
])
def test_get_coin_combination(cents : int, expected : list) -> None:
    assert get_coin_combination(cents) == expected


def test_large_amount() -> None:
    assert get_coin_combination(1000) == [0, 0, 0, 40]
