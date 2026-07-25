import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin, coin_conversion",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_some(coin: int, coin_conversion: list) -> None:
    assert get_coin_combination(coin) == coin_conversion
