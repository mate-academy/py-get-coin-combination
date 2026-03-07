import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (9, [4, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (24, [4, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2]),
    (100, [0, 0, 0, 4]),
    (99, [4, 0, 2, 3]),
    (41, [1, 1, 1, 1]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_result_has_four_elements() -> None:
    assert len(get_coin_combination(99)) == 4


def test_large_value() -> None:
    assert get_coin_combination(1000) == [0, 0, 0, 40]