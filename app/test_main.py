import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin, result", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (1237, [2, 0, 1, 49])
    ]
)
def test_get_coin_combination(coin: int, result: list) -> None:
    assert get_coin_combination(coin) == result
