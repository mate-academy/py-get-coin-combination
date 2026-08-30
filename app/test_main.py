import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("coin, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3])
])
def test_coins(coin: int, expected: list) -> None:
    assert get_coin_combination(coin) == expected
