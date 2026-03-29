import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="check_penny"),
        pytest.param(5, [0, 1, 0, 0], id="check_nickel"),
        pytest.param(10, [0, 0, 1, 0], id="check_dime"),
        pytest.param(25, [0, 0, 0, 1], id="check_quarter"),
        pytest.param(2, [2, 0, 0, 0], id="check_two_penny"),
        pytest.param(6, [1, 1, 0, 0], id="check_penny_and_nickel"),
        pytest.param(17, [2, 1, 1, 0], id="check_combination"),
        pytest.param(26, [1, 0, 0, 1], id="check_penny_and_quarter"),
        pytest.param(50, [0, 0, 0, 2], id="check_two_quarters"),

    ]
)
def test_get_coins(cents: int, result: list[int]) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"Get coin combination from {cents} should be equal to {result}"
