import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combinations(cents: int, expected: list) -> None:
    result = get_coin_combination(cents=cents)
    assert result == expected, f"Expected {expected}, but got {result}"
