import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero cents"),
        pytest.param(1, [1, 0, 0, 0], id="only pennies"),
        pytest.param(5, [0, 1, 0, 0], id="only nickel"),
        pytest.param(10, [0, 0, 1, 0], id="only dime"),
        pytest.param(25, [0, 0, 0, 1], id="only quarter"),
        pytest.param(6, [1, 1, 0, 0], id="penny and nickel"),
        pytest.param(17, [2, 1, 1, 0], id="pennies, nickel and dime"),
        pytest.param(41, [1, 1, 1, 1], id="one coin of each type"),
        pytest.param(50, [0, 0, 0, 2], id="two quarters"),
        pytest.param(99, [4, 0, 2, 3], id="max coins below a dollar"),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
