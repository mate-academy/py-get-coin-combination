import pytest
from app.main import get_coin_combination
from typing import Type


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "coins_are_zero",
        "coins_are_positive",
        "smallest possible number of pennies used",
        "smallest possible number of nickels used",
        "smallest possible number of coins used"
    ]
)
def test_get_human_age(cents: int, result: list[int]) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"Number of pennies, nickels, dimes and quarters should be: {result}"


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        ("20", TypeError),
        ([50], TypeError),
        ((20, 50), TypeError),
        ({20: 50}, TypeError)
    ],
    ids=[
        "raise_type_error_if_cents_are_string",
        "raise_type_error_if_cents_are_list",
        "raise_type_error_if_cents_are_tuple",
        "raise_type_error_if_cents_are_dictionary"
    ]
)
def test_raises_error_correctly(
        cents: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
