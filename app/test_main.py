import pytest

from app.main import get_coin_combination



@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="Test should return one penny"),
        pytest.param(6, [1, 1, 0, 0], id="Test should return one penny and one nickel"),
        pytest.param(17, [2, 1, 1, 0], id="Test should return three different coins"),
        pytest.param(50, [0, 0, 0, 2], id="Test should return only biggest coins")
    ]
)
def test_should_return_the_least_number_of_coins(cents: int, expected_result) -> None:
    result = get_coin_combination(cents)
    assert result == expected_result