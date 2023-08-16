from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,penny,nickel,dime,quarter",
    [
        (0, 0, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (6, 1, 1, 0, 0),
        (17, 2, 1, 1, 0),
        (50, 0, 0, 0, 2)
    ],
    ids=[
        "check result when 0 cents",
        "check penny in cents",
        "check nickel in cents",
        "check dimes in cents",
        "check quarter in cents"
    ]
)
def test_should_check_get_coin_combination(
    cents: int,
    penny: int,
    nickel: int,
    dime: int,
    quarter: int
) -> None:
    assert get_coin_combination(cents) == [penny, nickel, dime, quarter]
