from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, penny, nickel, dime, quarters",
    [
        (8, 3, 1, 0, 0),
        (13, 3, 0, 1, 0),
        (32, 2, 1, 0, 1),
        (4, 4, 0, 0, 0),
        (5, 0, 1, 0, 0),
        (10, 0, 0, 1, 0),
        (25, 0, 0, 0, 1)
    ]
)
def test_all_get_coin_combination(
        cents: int,
        penny: int,
        nickel: int,
        dime: int,
        quarters: int
) -> None:
    assert get_coin_combination(cents) == [penny, nickel, dime, quarters]
