from typing import Type

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "test_no_cents_should_return_all_coin_0",
        "test_1_cents_should_return_1_penny",
        "test_6_cents_should_return_1_penny_1_nickel",
        "test_17_cents_should_return_2_pennies_1_nickel_1_dime",
        "test_50_cents_should_return_2_quarters"
    ]
)
def test_calculation_get_coin_combination(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        pytest.param("1", TypeError, id="cents_should_be_int_not_str")
    ]
)
def test_raising_errors_correctly(
        cents: int | str,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
