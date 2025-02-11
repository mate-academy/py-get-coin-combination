from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="should_return_zero_coins_when_input_is_zero"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="should_return_one_penny_when_input_is_one"
        ),

        pytest.param(
            5, [0, 1, 0, 0],
            id="should_return_one_nickel_when_input_is_five"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="should_return_one_dime_when_input_is_ten"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="should_return_one_quarter_when_input_is_25"
        ),

        pytest.param(
            6, [1, 1, 0, 0],
            id="should_return_penny_and_nickel_when_input_is_six"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="should_return_optimal_combination_when_input_is_17"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="should_return_two_quarters_when_input_is_50"
        ),
        pytest.param(
            99, [4, 0, 2, 3],
            id="should_return_optimal_combination_when_input_is_99"
        ),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "amount",
    [
        pytest.param(
            1000,
            id="should_handle_thousand_cents"
        ),
        pytest.param(
            9999,
            id="should_handle_max_test_amount"
        ),
    ]
)
def test_large_amounts(amount: int) -> None:
    result = get_coin_combination(amount)
    total = (result[0] * 1
             + result[1] * 5
             + result[2] * 10
             + result[3] * 25)
    assert total == amount
