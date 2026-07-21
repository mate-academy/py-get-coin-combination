import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,pennies,nickels,dimes,quarters",
    [
        (4, 4, 0, 0, 0),
        (9, 4, 1, 0, 0),
        (19, 4, 1, 1, 0),
        (41, 1, 1, 1, 1)
    ],
    ids=[
        "should return only pennies, if `cents` < 5",
        "should return pennies and nickels, if (5 < `cents` < 10)",
        "should return coins except quarters, if (10 < `cents` < 20)",
        "should return all coins"
    ]
)
def test_get_coin_combination(cents: int, pennies: int, nickels: int,
                              dimes: int, quarters: int) -> None:
    assert get_coin_combination(cents) == [pennies, nickels, dimes, quarters]
