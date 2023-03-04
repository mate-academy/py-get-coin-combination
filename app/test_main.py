import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],

    ids=[
        "return list of zeros when input is 0",
        "return list of 1 penny when input is 1",
        "return list of 1 penny + 1 nickel when input is 6",
        "return 2 pennies, 1 nickel, 1 dime when input is 17",
        "return 2 quarters when input is 50"
    ]
)
def test_get_coin_combination(cents: int, expected_coins: list[int]) -> None:
    assert get_coin_combination(cents) == expected_coins


def test_raises_error_when_negative_value() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)
