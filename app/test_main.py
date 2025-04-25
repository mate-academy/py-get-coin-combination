import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),        # penny
        (5, [0, 1, 0, 0]),        # nickel
        (10, [0, 0, 1, 0]),       # dime
        (25, [0, 0, 0, 1]),       # quarter
        (6, [1, 1, 0, 0]),        # penny + nickel
        (30, [0, 1, 0, 1]),       # nickel + quarter
        (41, [1, 1, 1, 1]),       # 1 of each
    ]
)

def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
