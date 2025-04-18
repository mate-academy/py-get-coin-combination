import pytest

from .main import get_coin_combination


@pytest.mark.parametrize(
    "number_of_cents, expected_output",
    [
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2])
    ],
    ids=[
        "should return exactly 1 penny",
        "should return penny and nickel",
        "should return dime, 2 pennies and nickel",
        "should return 2 quarters"
    ]
)
def test_correctness_of_coins_conversion(number_of_cents, expected_output) -> None:
    assert get_coin_combination(number_of_cents) == expected_output
