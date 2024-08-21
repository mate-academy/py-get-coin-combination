import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expectation",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "test_should_return_1_penny_when_value_is_1",
        "test_should_return_1_penny_and_1_nickel_when_value_is_6",
        "test_should_return_2_pennies_1_nickel_and_1_dime_when_value_is_17",
        "test_should_return_2_quarters_when_value_is_50",
    ]
)
def test_get_coin_combination(
        cents: int,
        expectation: list
) -> None:
    assert get_coin_combination(cents) == expectation
