import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_combination",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (7, [2, 1, 0, 0]),
        (31, [1, 1, 0, 1]),
        (0, [0, 0, 0, 0])
    ]
)
def test_get_coin_combination(cents: int, expected_combination: list) -> None:
    assert get_coin_combination(cents) == expected_combination
