from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (6, [1, 1, 0, 0]),
        (41, [1, 1, 1, 1]),
        (42, [2, 1, 1, 1]),
        (101, [1, 0, 0, 4]),
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
