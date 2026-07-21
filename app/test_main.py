import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (6, [1, 1, 0, 0]),
    (42, [2, 1, 1, 1]),
    (100, [0, 0, 0, 4])
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert (
        get_coin_combination(cents) == expected
    ), f"Test should return {expected} if cents == {cents}"
