import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [pytest.param(0, [0, 0, 0, 0], id="zero_cents"),
     pytest.param(1, [1, 0, 0, 0], id="one_penny"),
     pytest.param(6, [1, 1, 0, 0], id="one_penny_one_nickel"),
     pytest.param(17, [2, 1, 1, 0], id="two_pennies_one_nickel_one_dime"),
     pytest.param(50, [0, 0, 0, 2], id="two_quarters"),
     pytest.param(100, [0, 0, 0, 4], id="four_quarters")]
)
def test_return_pennies(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
