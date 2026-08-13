from typing import Any

import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        pytest.param(0, [0, 0, 0, 0], id="0 cents gives no coins"),
        pytest.param(1, [1, 0, 0, 0], id="1 cent gives 1 penny"),
        pytest.param(
            4, [4, 0, 0, 0],
            id="4 cents give 4 pennies and no nickel"
        ),
        pytest.param(5, [0, 1, 0, 0], id="5 cents give 1 nickel"),
        pytest.param(
            6, [1, 1, 0, 0],
            id="6 cents give 1 penny and 1 nickel"
        ),
        pytest.param(
            9, [4, 1, 0, 0],
            id="9 cents give 4 pennies and 1 nickel, no dime"
        ),
        pytest.param(10, [0, 0, 1, 0], id="10 cents give 1 dime"),
        pytest.param(
            17, [2, 1, 1, 0],
            id="17 cents give 2 pennies, 1 nickel and 1 dime"
        ),
        pytest.param(
            24, [4, 0, 2, 0],
            id="24 cents give 4 pennies and 2 dimes, no quarter"
        ),
        pytest.param(25, [0, 0, 0, 1], id="25 cents give 1 quarter"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents give 2 quarters"),
        pytest.param(
            99, [4, 0, 2, 3],
            id="99 cents give 4 pennies, 2 dimes and 3 quarters"
        ),
        pytest.param(
            1000000, [0, 0, 0, 40000],
            id="large amount is converted into quarters only"
        ),
    ]
)
def test_should_return_smallest_number_of_coins(
        cents: int,
        expected_coins: list
) -> None:
    assert main.get_coin_combination(cents) == expected_coins


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param("25", id="string amount raises TypeError"),
        pytest.param(None, id="none amount raises TypeError"),
    ]
)
def test_should_raise_type_error_on_wrong_data_type(cents: Any) -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination(cents)
