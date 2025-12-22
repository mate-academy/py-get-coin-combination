from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "amount, expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(amount: int, expected: list[int]) -> None:
    assert get_coin_combination(amount) == expected