import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_value, expected_result",
    [
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2])
    ],
    ids=[
        "quantity of pennies should be 1",
        "quantity should be 1 penny + 1 nickel",
        "quantity should be 2 pennies + 1 nickel + 1 dime",
        "quantity should be 2 quarters"
    ]
)
def test_check_quantity_of_coins(
        input_value: int,
        expected_result: list) -> None:
    assert get_coin_combination(input_value) == expected_result
