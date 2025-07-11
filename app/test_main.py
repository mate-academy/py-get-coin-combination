import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_value,result",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero-cents"),
        pytest.param(1, [1, 0, 0, 0], id="one-penny"),
        pytest.param(6, [1, 1, 0, 0], id="one-nickel-one-penny"),
        pytest.param(16, [1, 1, 1, 0], id="dime-nickel-penny"),
        pytest.param(19, [4, 1, 1, 0], id="complex-19-cents"),
        pytest.param(24, [4, 0, 2, 0], id="two-dimes-four-pennies"),
        pytest.param(26, [1, 0, 0, 1], id="one-quarter-one-penny"),
        pytest.param(50, [0, 0, 0, 2], id="two-quarters")
    ]
)
def test_get_coin_combination_with_valid_values(
    input_value: int,
    result: list
) -> None:
    assert get_coin_combination(input_value) == result
