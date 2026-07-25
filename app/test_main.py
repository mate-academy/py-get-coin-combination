import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,pennies,nickels,dimes,quarters",
    [
        (1, 1, 0, 0, 0),
        (6, 1, 1, 0, 0),
        (17, 2, 1, 1, 0),
        (50, 0, 0, 0, 2),
    ],
    ids=[
        "1 cent should convert to 1 penny",
        "6 cents should convert to 1 penny and 1 nickel",
        "17 cents should convert to 2 pennies, 1 nickel and 1 dime",
        "50 cents should convert to 2 quarters",
    ]
)
def test_coin_combination(cents: int,
                          pennies: int,
                          nickels: int,
                          dimes: int,
                          quarters: int) -> None:
    assert (get_coin_combination(cents)
            == [pennies, nickels, dimes, quarters])
