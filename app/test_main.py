from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coin, expected",
    [
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_coin_combination(coin: int, expected: list[int]) -> None:
    assert get_coin_combination(coin) == expected
