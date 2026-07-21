import pytest
from app.main import get_coin_combination


test_cases = [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])
]


@pytest.mark.parametrize("cents, expected_coins", test_cases)
def test_get_coin_combination(cents: int, expected_coins: int) -> None:
    result = get_coin_combination(cents)
    assert result == expected_coins
