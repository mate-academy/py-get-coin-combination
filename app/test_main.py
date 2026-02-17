import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (8, [3, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (13, [3, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (22, [2, 0, 2, 0]),
        (36, [1, 0, 1, 1]),
        (40, [0, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (60, [0, 0, 1, 2]),
        (123, [3, 0, 2, 4])
    ]
)
def test_get_coin_combination(coin: int, expected: list[int]) -> None:
    assert get_coin_combination(coin) == expected
