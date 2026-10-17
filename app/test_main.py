import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero cents gives no coins"),
        pytest.param(1, [1, 0, 0, 0], id="1 cent gives 1 penny"),
        pytest.param(4, [4, 0, 0, 0], id="4 cents gives 4 pennies"),
        pytest.param(5, [0, 1, 0, 0], id="5 cents gives 1 nickel"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents gives penny and nickel"),
        pytest.param(10, [0, 0, 1, 0], id="10 cents gives 1 dime"),
        pytest.param(17, [2, 1, 1, 0], id="17 cents gives mixed coins"),
        pytest.param(25, [0, 0, 0, 1], id="25 cents gives 1 quarter"),
        pytest.param(41, [1, 1, 1, 1], id="41 cents gives one of each"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents gives 2 quarters"),
        pytest.param(99, [4, 0, 2, 3], id="99 cents gives mixed coins"),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
