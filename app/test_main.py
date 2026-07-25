import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        (-15, [0, 0, 0, 0])
    ],
)
def test_get_coin_combination(cents: int, expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins
