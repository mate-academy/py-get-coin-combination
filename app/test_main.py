import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        [0, [0, 0, 0, 0]],
        [1, [1, 0, 0, 0]],
        [5, [0, 1, 0, 0]],
        [6, [1, 1, 0, 0]],
        [10, [0, 0, 1, 0]],
        [16, [1, 1, 1, 0]],
        [25, [0, 0, 0, 1]],
        [26, [1, 0, 0, 1]],
        [30, [0, 1, 0, 1]],
        [31, [1, 1, 0, 1]],
        [36, [1, 0, 1, 1]],
        [41, [1, 1, 1, 1]],
        [50, [0, 0, 0, 2]]
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
