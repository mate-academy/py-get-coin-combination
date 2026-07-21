from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "input_values, expected_result",
    [
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(0, [0, 0, 0, 0]),
        pytest.param(41, [1, 1, 1, 1]),
        pytest.param(291, [1, 1, 1, 11])
    ]
)
def test_coins_combinations(
        input_values: int,
        expected_result: list
) -> None:
    assert (
        get_coin_combination(input_values) == expected_result
    )
