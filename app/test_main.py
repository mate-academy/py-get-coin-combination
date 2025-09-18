from app.main import get_coin_combination
import pytest


@pytest.fixture
def coins():
    return [0, 0, 0, 0] # [penny, nickel, dime, quarter]


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
]
)
def test_get_coin_combination(cents, expected, coins):
    assert get_coin_combination(cents) == expected
