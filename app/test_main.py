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
        (75, [0, 0, 0, 3]),
        (80, [0, 1, 0, 3]),
        (64, [4, 0, 1, 2]),
        (96, [1, 0, 2, 3]),
    ]
)
def test_get_coin_combination(cents: int, expected_coins: list) -> None:
    assert expected_coins == get_coin_combination(cents)
