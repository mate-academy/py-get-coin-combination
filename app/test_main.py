from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize("cents, expected_coins", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])])
def test_should_return_different_ages(cents: int,
                                      expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins
