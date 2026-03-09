from app.main import get_coin_combination


import pytest


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (69, [4, 1, 1, 2]),
    (266, [1, 1, 1, 10])
])
def test_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
