import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, result",
    [
        pytest.param(0, [0, 0, 0, 0], id="0 cent equal 0 penny"),
        pytest.param(1, [1, 0, 0, 0], id="1 cent equal 1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents equal 1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="17 cents equal "
                                          "2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents equal 2 quarters"),
    ]
)
def test_equal(cent: int, result: list) -> None:
    assert get_coin_combination(cent) == result
