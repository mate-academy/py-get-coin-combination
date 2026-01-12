import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount_of_cents,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (143, [3, 1, 1, 5])
    ],
    ids=[
        "should return zeros when amount of cents is zero",
        "should return 4 pennies when amount of cents is 4",
        "should return 1 nickel when amount of cents is 5",
        "should return 1 nickel and 4 pennies when amount of cents is 9",
        "should return 1 dime when amount of cents is 10",
        "should return 2 dimes and 4 pennies when amount of cents is 24",
        "should return 1 quarter when amount of cents is 25",
        "should return an expected result when amount of cents is a big value",
    ]
)
def test_with_different_amount_of_cents(
        amount_of_cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(amount_of_cents) == expected_result


def test_should_raise_error_when_cents_is_not_number() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("empty parameters")
