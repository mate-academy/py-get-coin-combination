import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_amount, result",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="should be 1 penny, 0 nickels, 0 dimes, 0 quarters in 1 cent"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should be 1 penny, 1 nickel, 0 dimes, 0 quarters in 6 cents"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="should be 0 pennys, 0 nickels, 1 dime, 0 quarters in 10 cents"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="should be 2 pennys, 1 nickel, 1 dime, 0 quarters in 17 cents"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="should be 1 penny, 1 nickel, 1 dime, 1 quarter in 41 cents"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="should be 0 pennys, 0 nickels, 0 dimes, 2 quarters in 50 cents"
        ),
        pytest.param(
            123, [3, 0, 2, 4],
            id="should be 3 pennys, 0 nickels, 2 dimes, 4 quarters in 123 \
cents"
        ),
        pytest.param(
            -3, [2, 0, 2, -1],
            id="should give negative number of coins for negetive cents amount"
        ),
        pytest.param(
            True, [1, 0, 0, 0],
            id="should be 1 penny, 0 nickels, 0 dimes, 0 quarters \
when 'True' given"
        ),
        pytest.param(
            False, [0, 0, 0, 0],
            id="should be 0 pennys, 0 nickels, 0 dimes, 0 quarters \
when 'True' given"
        ),
    ]

)
def test_for_valid_input_data(cents_amount: int, result: list) -> None:
    assert get_coin_combination(cents_amount) == result


@pytest.mark.parametrize(
    "cents_amount, expected_error",
    [
        pytest.param(
            "10", TypeError,
            id="cents amount should not be a string"
        ),
        pytest.param(
            [17], TypeError,
            id="cents amount should not be a list"
        ),
        pytest.param(
            (1, 0), TypeError,
            id="cents amount should not be a tuple"
        ),
        pytest.param(
            {"coins": 1}, TypeError,
            id="cents amount should not be a dict"
        ),
        pytest.param(
            {21}, TypeError,
            id="cents amount should not be a set"
        )
    ]
)
def test_error_codes(cents_amount: Any, expected_error: type) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents_amount)
