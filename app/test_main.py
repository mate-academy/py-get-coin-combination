from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 cent: 1 penny"),
        pytest.param(15, [0, 1, 1, 0], id="15 cents: 1 nickel, 1 dime"),
        pytest.param(17, [2, 1, 1, 0], id="17 cents: 2 dimes, "
                                          "1 nickel, 1 penny"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents: 2 quarters"),
        pytest.param(99, [4, 0, 2, 3], id="99 cents: 3 quarters, "
                                          "2 dimes, 4 pennies")
    ]
)
def test_return_different_coin_types(cents: int,
                                     result: list[int]) -> None:
    assert get_coin_combination(cents) == result
