from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 penny test"),
        pytest.param(6, [1, 1, 0, 0], id="1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
        pytest.param(51, [1, 0, 0, 2], id="1 penny + 2 quarter"),
    ],
)
def test_get_coin_combination(cents: int, result: list) -> None:
    """
    Test that the get_coin_combination function returns the correct result
    """
    assert get_coin_combination(cents) == result
