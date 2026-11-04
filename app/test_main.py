import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),      # zero: nothing to return
        (1, [1, 0, 0, 0]),      # one penny
        (4, [4, 0, 0, 0]),      # just below a nickel
        (5, [0, 1, 0, 0]),      # exactly one nickel
        (9, [4, 1, 0, 0]),      # nickel + pennies
        (10, [0, 0, 1, 0]),     # exactly one dime
        (17, [2, 1, 1, 0]),     # three coin types mixed
        (24, [4, 0, 2, 0]),     # just below a quarter
        (25, [0, 0, 0, 1]),     # exactly one quarter
        (41, [1, 1, 1, 1]),     # all four coin types
        (50, [0, 0, 0, 2]),     # two quarters
        (100, [0, 0, 0, 4]),    # many quarters
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
