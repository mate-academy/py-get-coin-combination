import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),  # 1 penny
        (5, [0, 1, 0, 0]),  # 1 nickel
        (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
        (10, [0, 0, 1, 0]),  # 1 dime
        (25, [0, 0, 0, 1]),  # 1 quarter
        (41, [1, 1, 1, 1]),  # 1 of each
    ]
)
def test_which_calculates_coins(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected


def tests_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
