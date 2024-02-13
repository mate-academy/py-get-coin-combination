from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "amount, result",
    [
        pytest.param(0, [0, 0, 0, 0],
                     id="Test with value = 0"),
        pytest.param(1, [1, 0, 0, 0],
                     id="Test when need to get penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="Test when need to get penny and nickel"),
        pytest.param(17, [2, 1, 1, 0],
                     id="Test when need to get penny and nickel and dime"),
        pytest.param(41, [1, 1, 1, 1],
                     id="Test when need to get penny "
                        "and nickel and dime and quarters"),
        pytest.param(50, [0, 0, 0, 2],
                     id="Test when need to get quarters")
    ]
)
def test_get_coin_combination(amount: int, result: list[int]) -> None:
    assert (get_coin_combination(amount) == result), \
        f"Result function with value: {amount} should be equal to {result}"
