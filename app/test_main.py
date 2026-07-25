import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "test_value,expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="Function returns only pennies"),
        pytest.param(5, [0, 1, 0, 0], id="Function returns only nickels"),
        pytest.param(20, [0, 0, 2, 0], id="Function returns only dimes"),
        pytest.param(100, [0, 0, 0, 4], id="Function returns only nickels"),
        pytest.param(66, [1, 1, 1, 2], id="Function returns all coins"),
        pytest.param(0, [0, 0, 0, 0], id="Function returns no coins")
    ]
)
def test_function_get_coin_combination(
        test_value: int,
        expected_result: int
) -> None:
    assert get_coin_combination(test_value) == expected_result
