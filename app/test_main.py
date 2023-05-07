import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero is equal to zeroes"),
        pytest.param(3, [3, 0, 0, 0], id="test pennies only"),
        pytest.param(5, [0, 1, 0, 0], id="test nickel only"),
        pytest.param(10, [0, 0, 1, 0], id="test dime only"),
        pytest.param(25, [0, 0, 0, 1], id="test quarter only"),
        pytest.param(116, [1, 1, 1, 4], id="test every types"),
    ]
)
def test_some_combinations(cents: int, result: list) -> None:
    assert (get_coin_combination(cents) == result
            ), f"{cents} should be equal to {result}"
