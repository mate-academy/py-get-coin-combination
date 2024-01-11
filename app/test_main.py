from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "initial_input,expected_result",
    [
        pytest.param(
            3, [3, 0, 0, 0],
            id="should be pennies when cents less than 5"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="should be only nickels when cents equals to 5"
        ),
        pytest.param(
            8, [3, 1, 0, 0],
            id="should be pennies and nickels when cents in range 5 - 10"
        ),
        pytest.param(
            20, [0, 0, 2, 0],
            id="should be only dimes when cents less then 25 and divided by 10"
        ),
        pytest.param(
            18, [3, 1, 1, 0],
            id="should be pennies nickels and dimes when cents less than 25"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="should be only quarters when cents divisible by 25"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="should return all coins when cents equal to 41"
        ),
    ]
)
def test_should_return_correct_list(
        initial_input: int,
        expected_result: list
) -> None:
    assert get_coin_combination(initial_input) == expected_result
