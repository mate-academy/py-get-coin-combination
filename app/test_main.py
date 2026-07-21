import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    ("cents", "expected"),
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (17, [2, 1, 1, 0]),
    ],
)
def test_get_coin_combination(cents: int,
                              expected: list[int]) -> None:
    error_message = f"Function should return {expected} when {cents}"
    assert get_coin_combination(cents) == expected, error_message
