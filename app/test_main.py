import pytest as pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coin_combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),

    ],
    ids=[
        "1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "2 quarters",
    ]
)
def test_can_sum(cents: int, coin_combination: list) -> None:
    assert get_coin_combination(cents) == coin_combination
