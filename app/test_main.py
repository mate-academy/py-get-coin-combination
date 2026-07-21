import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
        (4, [4, 0, 0, 0]),
        (125, [0, 0, 0, 5]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
