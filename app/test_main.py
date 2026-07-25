from app.main import get_coin_combination
import pytest


# write your tests here
@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2])
])
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected
