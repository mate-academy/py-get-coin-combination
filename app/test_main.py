import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(0, [0, 0, 0, 0], id="zeroes"),
        pytest.param(1, [1, 0, 0, 0], id="test pennies only"),
        pytest.param(5, [0, 1, 0, 0], id="test nickel only"),
        pytest.param(10, [0, 0, 1, 0], id="test dime only"),
        pytest.param(25, [0, 0, 0, 1], id="test quarter only"),
        pytest.param(42, [2, 1, 1, 1], id="test every types"),
        pytest.param(67, [2, 1, 1, 2], id="test every types over 1"),
    ],
)
def test_variants(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"{cents} should be equal to {result}"
