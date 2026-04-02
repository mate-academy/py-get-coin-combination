from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3])
])
def test_get_coin_combination_return_coins_of_different_types(
        cents: int, expected: list
) -> None:
    assert get_coin_combination(cents) == expected
