import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(1, [1, 0, 0, 0], id="cents_to_penny"),
        pytest.param(6, [1, 1, 0, 0], id="cents_to_penny_nickel"),
        pytest.param(17, [2, 1, 1, 0], id="cents_to_penny_nickel_dime"),
        pytest.param(50, [0, 0, 0, 2], id="cents_to_quarters"),
    ]
)
def test_cents_another_coin(cents: int, result: list) -> None:
    assert (get_coin_combination(cents) == result)
